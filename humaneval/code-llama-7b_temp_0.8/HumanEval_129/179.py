
def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    # 注意k至少为grid的长度
    if k < len(grid):
        return None

    # 最优解肯定是最短路径, 因此可以用DFS搜索整个图
    # 这里借用DFS求解最短路径, 初始化方程为:
    # D[x][y] = min(D[x-1][y], D[x][y-1]) + grid[x][y]
    # 对于图的第一行和第一列, 由于不能走出图, 需要初始化为:
    # D[0][0] = 0
    # D[i][0] = D[i-1][0] + grid[i][0]
    # D[0][j] = D[0][j-1] + grid[0][j]
    # 
    # 我们可以从任意位置开始搜索, 最短路径必定从起点出发
    # 递归搜索时, 我们需要记录一下搜索过程中的最小值
    # 对于每一个格子, 我们记录D[x][y]表示沿着路径遍历x, y
    # 格子的路径需要知道x, y的前一个位置的最小值和当前位置的值
    # 因此我们可以使用递归搜索的方式记录, 当然我们可以使用迭代来
    # 记录最短路径
    # 时间复杂度: O(N*N*k) 空间复杂度: O(N*N)
    # 我们可以用一个矩阵来存储每一个格子的最短路
