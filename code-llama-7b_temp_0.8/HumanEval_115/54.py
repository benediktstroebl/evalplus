
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
    # length of the grid
    grid_length = len(grid)
    # length of the column
    grid_column = len(grid[0])

    # initialise the water left in the grid
    water_left = 0
    # initialise the number of lowering needed
    number_of_lowering = 0

    # calculate the total water left in the grid
    for i in range(grid_length):
        for j in range(grid_column):
            water_left += grid[i][j]
    
    # calculate the amount of water need to extract
    water_extracted = water_left - capacity * grid_length

    # check if the water left is greater than 0
    if water_extracted > 0:
        # find the number of times the lowering is needed
        number_of_lowering = water_extracted / grid_length
        # calculate the number of water left in the grid after lowering
        water_left -= number_of_lowering * grid_length
        # calculate the number of water left in the last row
        water_last_row = water_left - (number_of_lowering * (grid_length - 1))

    # check if the water left is greater than 0
    if water_last_row > 0:
        # find the number of times the lowering is needed
        number_of_lowering += math.ceil(water_last_row / grid_column)
    
    return number_of_lowering

