
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    n = len(grid)
    m = len(grid[0])

    # attempt 2: DP, O(mn^2) time
    # visited = [[False for _ in range(m)] for _ in range(n)]
    # # for each row, for each col, find the max of the array
    # # after filling, remove the max value row
    # def stack(row, col):
    #     if visited[row][col]: return 0
    #     res = 0
    #     visited[row][col] = True
    #     for i in range(0, m):
    #         res = max(res, grid[row][i])
    #         if visited[row][i]:
    #             res = max(res, grid[i][col])
    #     stack(row+1, col)
    #     stack(row-1, col)
    #     stack(row, col+1)
    #     stack(row, col-1)
    #     for i in range(0, n):
    #         for j in range(0, m):
    #             grid[i][j] -= res
    # print(grid)
    # for i in range(0, n):
    #     for j in range(0, m):
    #         stack(i, j)


    # attempt 3: DP, O(mn) time
    # the rows, cols represent the max water in the wells
    # for each row, col, the max of the columns is the well
    # when we remove a row, set that well to the previous max, and we
    # remove the max of the row
    n, m = len(grid), len(grid[0])
    res = [[0 for _ in range(m)] for _ in range(n)]
    stack = [0 for _ in range(n)]
    for row in range(n-1, -1, -1):
        for col in range(m-1, -1, -1):
            stack[row] = max(stack[row], grid[row][col])
            res[row][col] = stack[row]
        for col in range(m-1, -1