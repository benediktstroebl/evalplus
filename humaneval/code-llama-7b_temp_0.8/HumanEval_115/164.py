
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

    if not grid: return 0

    width, height = len(grid[0]), len(grid)
    num_buckets = width - 1
    min_num_buckets = num_buckets
    buckets = [capacity] * num_buckets

    def can_empty_well(well, bucket, water_remaining):
        if (well + 1) * bucket <= water_remaining:
            return True
        return False

    def can_fill_well(well, bucket, water_remaining):
        if well >= 0 and grid[well][bucket] == 1:
            return True
        return False

    def is_full(buckets):
        if 0 in buckets: return False
        return True

    def find_empty_bucket(buckets):
        for bucket in range(0, len(buckets)):
            if buckets[bucket] == 0:
                return bucket
        return -1

    def find_full_bucket(buckets):
        for bucket in range(0, len(buckets)):
            if buckets[bucket] == capacity:
                return bucket
        return -1

    def find_empty_well(buckets):
        for well in range(height):
            for bucket in range(len(buckets)):
                if grid[well][bucket] == 1:
                    return well, bucket
        return -1, -1

    def find_full_well(buckets):
        for well in range(height):
            for bucket in range(len(buckets)):
                if grid[well][bucket] == 0:
                    return well, bucket
        return -1, -1

    def update_buckets(well, bucket, water_remaining):
        buckets[bucket] -= (well + 1)
        buckets[bucket + 1] += (width - (well + 2))
        return buckets

    def update_water_remaining(water_remaining, well, bucket):
        if grid[well][bucket] == 0:
            return water_remaining - ((width - (bucket + 2)) * (well + 1))
