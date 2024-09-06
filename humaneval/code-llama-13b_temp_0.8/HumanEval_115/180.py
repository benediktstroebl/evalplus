
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
    
    num_rows = len(grid)
    num_columns = len(grid[0])
    num_buckets = capacity

    if num_rows * num_columns < num_buckets:
        return 0

    # split into 3 wells
    # max of (left + right)
    # max of (top + bottom)
    # max of (top-left + bottom-right)
    # max of (top-right + bottom-left)
    max_left_right = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    max_top_bottom = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    max_top_left_bottom_right = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    max_top_right_bottom_left = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

    for i in range(num_rows):
        current_water = 0
        for j in range(num_columns):
            current_water += grid[i][j]
            max_left_right[i][j] = current_water

        current_water = 0
        for j in reversed(range(num_columns)):
            current_water += grid[i][j]
            max_top_bottom[i][j] = current_water

    for i in range(num_rows):
        current_water = 0
        for j in range(num_columns):
            current_water += grid[i][j]
            max_top_left_bottom_right[i][j] = current_water

    for i in range(num_rows):
        current_water = 0
        for j in reversed(range(num_columns)):
            current_water += grid[i][j]
            max_top_right_bottom_left[i][j] = current_water

    max_left_right = max_left_right[num_rows - 1]
    max_top_bottom = max_top_bottom[num_rows - 1
