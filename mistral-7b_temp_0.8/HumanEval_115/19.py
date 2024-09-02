
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
    max_y = len(grid)
    max_x = len(grid[0])
    row_count = 0
    col_count = 0
    for i in range(max_y):
        if grid[i].count(1) > 0:
            row_count = i
            break

    for j in range(max_x):
        if grid[row_count].count(1) > 0:
            col_count = j
            break

    # # Find the number of steps required to empty a bucket
    # def count_steps(row, col):
    #     steps = 0
    #     while grid[row][col] != 0:
    #         if grid[row][col] == 1:
    #             grid[row][col] = 0
    #             steps += 1
    #         else:
    #             row = row + 1
    #             col = col + 1
    #     return steps

    # # Count the total number of steps required to empty all buckets
    # total_steps = 0
