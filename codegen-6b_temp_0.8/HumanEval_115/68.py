
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
    # grid = grid.copy()
    # for i, row in enumerate(grid):
    #     row += row

    # for row in grid:
    #     max_row = max(row)
    #     for i, num in enumerate(row):
    #         row[i] += row.count(num)

    row_max = [[0] * capacity for _ in range(len(grid) + 1)]
    col_max = [[0] * capacity for _ in range(len(grid[0]) + 1)]

    # row_max[i][j] = max no. of wells that can be filled in row[0:i]: j
    # col_max[i][j] = max no. of wells that can be filled in col[0:j]
    for i in range(0, len(grid) + 1):
        for j in range(0, len(grid[0]) + 1):
            if i == 0 or j == 0:
                row_max[i][j] = 0
                col_max[i][j] = 0
            elif grid[i-1][j-1] == 1:
                row_max[i][j] = max(row_max[i][j-1], row_max[i-1][j]) + 1
                col_max[i][j] = max(col_max[i][j-1], col_max[i-1][j]) + 1
            else:
                row_max[i][j] = row_max[i][j-1]
                col_max[i][j] = col_max[i-1][j]

    # @lru_cache(None)
    def prepare(i, j):
        if i == 0 or j == 0:
            return 0
        if grid[i-1][j-1] == 1:
            return max(prepare(i-1, j), prepare(i, j-1)) + 1
        else:
            return prepare(i-1, j) + prepare(i, j-1)

    best = 0
    for i in range(len(grid)):
        for j in range(len(grid[0