
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
    row_count = len(grid)
    col_count = len(grid[0])
    row_index = 0
    col_index = col_count-1
    times = 0

    while row_index < row_count and col_index >= 0:
        if grid[row_index][col_index] != 0:
            water_in_well = grid[row_index][col_index]
            bucket_capacity_minus_one = capacity - 1
            times_needed_full_buckets = math.floor(min(water_in_well, bucket_capacity_minus_one)/bucket_capacity_minus_one)
            for time in range(times_needed_full_buckets):
                times += 1
                water_in_well -= bucket_capacity_minus_one
            if water_in_well <= bucket_capacity_minus_one:
                times += 1
                water_in_well = 0
            grid[row_index][col_index] = water_in_well
        row_index += 1
        col_index -= 1
    return times

