
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
    rows, cols = len(grid), len(grid[0])
    water_volume = sum((row.count(1) for row in grid))
    bucket_volume = water_volume // capacity
    bucket_remaining = water_volume % capacity
    time = bucket_remaining
    while bucket_remaining:
        bucket_remaining = 0
        for row in grid:
            b_i = res = 0
            while res < bucket_volume and b_i < cols:
                b_i = row.index(1, b_i)
                res += 1
                if res > bucket_volume:
                    time += bucket_volume
                    b_i = cols
                else:
                    time += res
                    bucket_remaining += res
                    b_i += 1
    return time
