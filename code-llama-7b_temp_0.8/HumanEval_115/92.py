
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
    rows = len(grid)
    cols = len(grid[0])
    buckets = capacity
    current_row = 0
    current_col = 0
    current_unit = 0
    num_moves = 0
    while True:
        # update variables
        current_unit = grid[current_row][current_col]
        buckets += current_unit
        # check if we are at the bottom of the grid
        if current_row == rows - 1:
            break
        # check if we are at the rightmost column and need to move to next row
        if current_col == cols - 1:
            current_row += 1
            current_col = 0
        else:
            current_col += 1

        # check if we need to move up
        if buckets == capacity:
            current_row -= 1
            current_col = 0
            buckets = 0
            num_moves += 1

    return num_moves
