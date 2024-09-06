
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
    # ============================================================================
    # Solution 1
    # ============================================================================
    # rows = len(grid)
    # cols = len(grid[0])
    # buckets = [[0] * cols for _ in range(rows)]
    # buckets[0] = grid[0]

    # for i in range(1, rows):
    #     for j in range(cols):
    #         buckets[i][j] = min(buckets[i - 1][j], grid[i][j])

    # for i in range(rows - 2, -1, -1):
    #     for j in range(cols):
    #         buckets[i][j] += buckets[i + 1][j]

    # return sum(map(sum, buckets))

    # ============================================================================
    # Solution 2
    # ============================================================================
    # rows = len(grid)
    # cols = len(grid[0])
    # buckets = grid

    # for i in range(1, rows):
    #     for j in range(cols):
    #         buckets[i][j] = min(buckets[i - 1][j], grid[i][j])

    # for i in range(rows - 2, -1, -1):
    #     for j in range(cols):
    #         buckets[i][j] += buckets[i + 1][j]

    # return sum(map(sum, buckets))

    # ============================================================================
    # Solution 3
    # ============================================================================
    rows = len(grid)
    cols = len(grid[0])
    buckets = grid

    for i in range(1, rows):
        for j in range(cols):
            buckets[i][j] = min(buckets[i - 1][j], grid[i][j])

    for i in range(rows - 2, -1, -1):
        for j in range(cols):
            buckets[i][j] = min(
