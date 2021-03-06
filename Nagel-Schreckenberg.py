# -*- coding: utf-8 -*-

import  matplotlib
from matplotlib.font_manager import *
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
np.random.seed(0)


def Run(path=5000, n=100, v0=20, ltv=60, p=0.3, times=3000):
    '''
    path  道路长度
    n  车辆数目
    v0  初始速度
    ltv  最大限速
    p  减速概率
    times 模拟的时刻数目
    '''

    # x保存每辆车在道路上的位置，随机初始化
    x = np.random.rand(n) * path
    x.sort()
    # v保存每辆车的速度，初速度相同
    v = np.ones(n) * v0

    plt.figure(figsize=(5, 4), facecolor='w')
    # 模拟每个时刻
    for t in range(times):
        plt.scatter(x, [t] * n, s=1, c='k', alpha=0.05)
        # 模拟每辆车
        for i in range(n):
            # 计算当前车与前车的距离，注意是环形车道
            if x[(i + 1) % n] > x[i]:
                d = x[(i + 1) % n] - x[i]
            else:
                d = path - x[i] + x[(i + 1) % n]
            # 根据距离计算下一秒的速度
            if v[i] < d:
                if np.random.rand() > p:
                    v[i] += 1
                else:
                    v[i] -= 1
            else:
                v[i] = d - 1
        # 对速度进行限制
        v = v.clip(0, ltv)

        # 一秒后，车辆的位置发生了变化
        x += v
        # 注意是环形车道
        x = x % path

    # 展示
    plt.xlim(0, path)
    plt.ylim(0, times)
    plt.xlabel(u'车辆位置')
    plt.ylabel(u'模拟时间')
    
    # plt.tight_layout(pad=2)
    plt.show()


    # Run(v0=0)
    # Run(v0=20)
    # Run(v0=40)
    # Run(v0=60)

    # Run(p=0.0)
    # Run(p=0.1)
    # Run(p=0.3)
Run(p=0.5)
# Run(p=0.8)
# Run(p=1.0)