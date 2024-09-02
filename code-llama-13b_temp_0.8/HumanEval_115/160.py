
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
    # # --- Brute Force --- #
    # water_count = 0
    # for row in grid:
    #     for well in row:
    #         if well == 1:
    #             water_count += 1
    # num_buckets = math.ceil(water_count / capacity)
    # return num_buckets
    
    # --- Divide and Conquer --- #
    # Find the middle row and column
    # Then divide and conquer on the left half and right half
    row_count = len(grid)
    col_count = len(grid[0])
    col_mid = col_count // 2
    row_mid = row_count // 2
    
    if row_count == 1 or col_count == 1:
        return sum(1 for row in grid for col in row if col == 1) // capacity
    else:
        num_left = max_fill(grid[:row_mid, :col_mid], capacity)
        num_right = max_fill(grid[:row_mid, col_mid:], capacity)
        num_down = max_fill(grid[row_mid:, :], capacity)
        return max(num_left, num_right, num_down)

