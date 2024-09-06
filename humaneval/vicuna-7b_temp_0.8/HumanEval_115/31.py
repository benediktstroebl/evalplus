
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
    row = len(grid)
    col = len(grid[0])
    row_sum = sum(grid)
    col_sum = sum(grid[0])
    max_val = max(grid)
    count = 0
    while row > 0 and col > 0:
        if grid[row-1][col-1] == 1 and grid[row-1][col] == 0:
            grid[row-1][col] = max_val
            grid[row-1][col-1] = 0
            grid[row-1][col+1] = 0
            grid[row][col-1] = 0
            grid[row][col+1] = 0
            grid[row+1][col-1] = 0
            grid[row+1][col] = 0
            grid[row+1][col+1] = 0
            grid[row-1][col+2] = 0
            grid[row][col-1] = max_val
            grid[row][col] = 0
            grid[row][col+1] = 0
            row -= 1
            col -= 1
            count += 1
        elif grid[row-1][col] == 1:
            grid[row-1][col] = max_val
            grid[row-1][col-1] = 0
            grid[row-1][col+1] = 0
            grid[row][col-1] = 0
            grid[row][col+1] = 0
            grid[row+1][col-1] = 0
            grid[row+1][col] = 0
            grid[row+1][col+1] = 0
            grid[row-1][col+2] = 0
            grid[row][col-1] = max_val
            grid[row][col] = 0
            grid[row][col+1] = 0
            count += 1
        else:
            break
    if row > 0 and col > 0:
        print(count)
    else:
        print(0)

max_fill(grid,
