
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
    def get_row_length(grid):
        return len(grid[0])
    def get_well_count(grid):
        return len(grid)
    def get_water(grid, i, j):
        return grid[i][j]
    def get_bucket_capacity():
        return capacity
    def get_row_index_with_most_water():
        max_water_index = 0
        max_water = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                water = get_water(grid, i, j)
                if water == 1:
                    row_water = 0
                    for k in range(len(grid[i])):
                        if grid[i][k] == 1:
                            row_water += 1
                    if row_water > max_water:
                        max_water = row_water
                        max_water_index = i
        return max_water_index
    def extract_water(grid, i, j, bucket_capacity):
        water = get_water(grid, i, j)
        if water == 1:
            for k in range(len(grid[i])):
                if grid[i][k] == 1:
                    grid[i][k] = 0
                    bucket_capacity -= 1
        return bucket_capacity

    bucket_capacity = get_bucket_capacity()
    max_water_index = get_row_index_with_most_water()
    for i in range(len(grid)):
        grid[i][0] = 0
    for j in range(len(grid[max_water_index])):
        bucket_capacity = extract_water(grid, max_water_index, j, bucket_capacity)
    if bucket_capacity == 0:
        return 0
    else:
        return math.ceil(bucket_capacity / capacity)
