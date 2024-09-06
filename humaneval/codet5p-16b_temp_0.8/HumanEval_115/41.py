
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

    bucket_capacity = capacity
    bucket_height = 0
    bucket_water_capacity = 0
    bucket_index = 0
    buckets_to_lower = 0
    water_height = 0

    for row in grid:
        for value in row:
            if value == 1:
                if bucket_height < bucket_capacity:
                    bucket_height += 1
                    bucket_water_capacity += 1
                    water_height += 1
                else:
                    bucket_index += 1
                    if bucket_index!= len(grid):
                        if bucket_water_capacity!= 0:
                            bucket_water_capacity = bucket_water_capacity - 1
                            bucket_water_capacity = math.floor(bucket_water_capacity/2)
                            bucket_water_capacity = bucket_water_capacity + 1
                            buckets_to_lower += 1
                            bucket_water_capacity = bucket_water_capacity - bucket_height
                            bucket_height = bucket_height - 1
                            bucket_water_capacity = bucket_water_capacity + bucket_height
                            buck
