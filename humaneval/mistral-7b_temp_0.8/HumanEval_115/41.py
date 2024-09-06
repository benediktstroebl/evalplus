
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
    row, col = len(grid), len(grid[0])
    f = [[0]*(col+1) for i in range(row+1)]
    f[0][1:] = grid[0][1:]

    for r in range(1, row):
        for c in range(1, col):
            f[r+1][c] = f[r][c] + f[r][c-1]

    res = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                if capacity >= f[r][c] and capacity <= f[r+1][c]:
                    res += 1
                elif capacity >= f[r][c-1] and capacity <= f[r+1][c]:
                    res += 1
    return res

