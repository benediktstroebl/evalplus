
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
    # Find the number of water filled in each row
    water_filled = []
    for row in grid:
        filled = 0
        for col in row:
            filled += col
        water_filled.append(filled)

    # Sort water filled
    sorted_water_filled = sorted(water_filled)

    # Number of buckets that can hold the maximum number of water
    number_of_buckets = math.ceil(sorted_water_filled[0] / capacity)
    # Number of times it takes to empty the grid
    number_of_times = 0
    for water_filled in sorted_water_filled:
        if water_filled % capacity == 0:
            water_filled = water_filled / capacity
        else:
            water_filled = water_filled / capacity + 1
        if water_filled > number_of_buckets:
            number_of_buckets = water_filled
            number_of_times += 1
    return number_of_times

