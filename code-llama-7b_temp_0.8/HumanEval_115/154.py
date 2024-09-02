
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

    def get_total_water(grid, bucket_capacity):
        total_water = 0
        for row in grid:
            total_water += sum(row)
        return total_water

    total_water = get_total_water(grid, bucket_capacity)

    if total_water == 0: return 0

    water_left = total_water
    num_buckets = math.ceil(total_water / bucket_capacity)
    num_buckets_used = 0

    for row in grid:
        # try to fill bucket with row
        while water_left > bucket_capacity:
            num_buckets_used += 1
            water_left -= bucket_capacity
            if water_left == 0: return num_buckets_used
        # now that bucket is full, try to fill with remaining water
        while water_left > 0:
            row[-1] -= 1
            water_left -= 1
            if water_left == 0: return num_buckets_used

    return num_buckets_used

