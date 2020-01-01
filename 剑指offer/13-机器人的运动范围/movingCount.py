# -*- coding:utf-8 -*-
"""
题目：
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


class Solution:

    def __init__(self):
        self.vis = []

    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.moving(threshold, rows, cols, 0, 0)

    def moving(self, threshold, rows, cols, i, j):
        """
        机器人已经移动到了坐标 （i, j），满足下面三个 if 条件的该格子就不能达到。
        把能达到的格子坐标记录到 vis 字典中，
        """
        if self.sumNumber(i) + self.sumNumber(j) > threshold:
            return 0
        if i >= rows or j >= cols or i < 0 or j < 0:
            return 0
        if (i, j) in self.vis:
            return 0
        self.vis.append((i, j))

        return 1 + self.moving(threshold, rows, cols, i - 1, j) \
               + self.moving(threshold, rows, cols, i + 1, j) \
               + self.moving(threshold, rows, cols, i, j - 1) \
               + self.moving(threshold, rows, cols, i, j + 1)

    def sumNumber(self, x):
        if x <= 0:
            return 0
        res = 0
        while x:
            res += x % 10
            x /= 10
        return res





