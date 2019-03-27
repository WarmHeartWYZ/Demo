# -*- coding: utf-8 -*-
"""
@author: 热心市民吴彦祖
"""
#定义一个比较大的值
MAX = 99999
#邻接矩阵
graph = [[0, 2, 3, MAX, MAX],
          [MAX, 0, MAX, 4, 5],
          [1, MAX, 0, 4, 5],
          [MAX, MAX, 3, 0, 5],
          [MAX, MAX, 3, 4, 0]]
#生成路径矩阵
def createPathMatrix(SIZE):
    PathMatrix = []
    tmp = []
    for i in range(SIZE):
        P = []
        for j in range(SIZE):
            P.append(list(tmp))
        PathMatrix.append(list(P))
    return PathMatrix
#基于Floyd算法生成最短路径矩阵
def Floyd(Matrix, PathMatrix):
    SIZE = len(Matrix)
    for k in range(SIZE):
        for i in range(SIZE):
            for j in range(SIZE):
                if (i == j) or (j == k) or (i == k):
                    continue
                s = Matrix[i][k] + Matrix[k][j]
                if s < Matrix[i][j]:
                    Matrix[i][j] = s
                    PathMatrix[i][j].append(k)#将经过的节点存入列表
    return Matrix, PathMatrix
#利用递归生成最短路径
def searchPath(start, target, pathMatrix):
    mid = pathMatrix[start][target]
    if len(mid) == 0:
        return []
    return searchPath(start, mid[-1], pathMatrix) + [mid[-1]] + searchPath(mid[-1], target, pathMatrix)

pathMatrix = createPathMatrix(len(graph))#生成路径矩阵
Matrix, pathMatrix = Floyd(graph, pathMatrix)#计算最短路径并更新路径矩阵
start = 0#出发节点
target = 4#终点节点
path = searchPath(start, target, pathMatrix)#搜索中间路径
output = [start] + path + [target]#生成完整路径
print(output)
