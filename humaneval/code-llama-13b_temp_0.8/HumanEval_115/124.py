
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
    grid = list(map(lambda x: list(map(int, x)), grid))
    rows = len(grid)
    cols = len(grid[0])

    # Find maximum depth of each well
    depths = []
    for col in range(cols):
        depth = 0
        for row in range(rows):
            depth += grid[row][col]
        depths.append(depth)

    # The solution is a divisor of max(depths).
    # Since we need to empty the wells, we need to do the opposite.
    max_depth = max(depths)
    # Find greatest common divisor for all max_depths
    # to find the number of buckets we need to use.
    # This will be the number of times we need to lower the buckets.
    gcd = max_depth
    for i in range(max_depth):
        if max_depth % i == 0:
            gcd = i
    return math.ceil(max_depth/gcd)

