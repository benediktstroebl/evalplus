
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
    if not grid:
        return 0

    m = len(grid)
    n = len(grid[0])

    # memoization:
    # mem[m][n] : minimum number of bucket lowering needed
    # to empty the m x n grid.
    mem = [[0] * n for _ in range(m)]

    # 1-dimentional array
    mem1 = [0] * n

    # 1-dimensional array
    mem2 = [0] * m

    mem[m-1][n-1] = grid[m-1][n-1]
    for i in range(m-2, -1, -1):
        mem[i][n-1] = grid[i][n-1] + mem[i+1][n-1]

    for j in range(n-2, -1, -1):
        mem[m-1][j] = grid[m-1][j] + mem[m-1][j+1]
    
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            mem[i][j] = grid[i][j] + min(mem[i+1][j], mem[i][j+1])

    return mem[0][0]

