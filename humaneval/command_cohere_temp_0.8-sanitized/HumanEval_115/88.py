import math
def max_fill(grid, capacity):
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
    # One dimensional arrays are converted to lists for python 3 compatibility
    grid = [list(row) for row in grid]

    if not grid:
        return 0

    # initialization
    m = len(grid)
    n = len(grid[0])
    count = 0
    buckets_needed = 0

    for i in range(m):
        row = grid[i]
        j = 0
        while j < n:
            if row[j] == 1:
                count += 1
                j += capacity - 1
            else:
                j += 1
        buckets_needed += count // capacity if count % capacity != 0 else count // capacity + 1

    return buckets_needed