
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
    max_wells = 0
    for row in grid:
        max_wells = max(max_wells, len(row))
    if max_wells == 0:
        return 0
    max_wells -= 1
    buckets = [0] * max_wells
    remainder = 0
    for row in grid:
        remainder += 1
        for i in range(max_wells):
            if remainder > 0:
                if row[i] == 1:
                    buckets[i] = min(buckets[i] + remainder, capacity)
                    remainder = 0
            else:
                break
    return sum([1 for bucket in buckets if bucket > 0]) - 1

