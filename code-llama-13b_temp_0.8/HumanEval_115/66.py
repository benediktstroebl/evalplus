
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
    
    total = 0
    for row in grid:
        for well in row:
            total += well
    if capacity < total:
        return math.inf
    
    # e.g. [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # Put buckets of capacity at the bottom, collecting the total amount of water
    # Then fill that bucket back up, and do the same, etc.
    
    # Max amount of water that could be collected, in the given capacity:
    max_fillable = sum([(math.ceil(row.count(1)/capacity) * capacity) for row in grid])
    # Now empty the buckets
    # From the bottom up, fill buckets up to capacity until max_fillable is reached
    total = 0
    for row in grid[::-1]:
        total += row.count(1)
        if total > max_fillable:
            break
        else:
            for i in range(0, row.count(1) // capacity):
                row[i::capacity] = [capacity] * (row.count(1) // capacity)
    return total

