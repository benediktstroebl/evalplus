
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
    def fill_until_full(bucket_capacity, water_level, water_count):
        current_bucket_water_level = water_count
        if current_bucket_water_level < bucket_capacity:
            current_bucket_water_level = bucket_capacity
        if water_level > 0:
            water_level -= bucket_capacity
            water_count += bucket_capacity
        if water_level > current_bucket_water_level:
            water_count += (water_level - current_bucket_water_level)
            water_level = current_bucket_water_level
        return water_count, water_level

    count = 0
    water_count = 0
    water_level = 0
    for row in grid:
        water_level += sum(row)
    if water_level == 0:
        return 0
    for row in grid:
        for water_amount in row:
            if water_level <= 0:
                break
            elif water_amount == 1:
                water_count += 1
            elif water_count >= 1:
                water_count, water_level = fill_until_full(
                    bucket_capacity, water_level, water_count)
            if water_level <= 0:
                break
            count += 1
    if water_level > 0:
        count += math.ceil(water_level / bucket_capacity)
    return count

