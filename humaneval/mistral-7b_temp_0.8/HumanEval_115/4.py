
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

    # Special case for all zeros
    if grid == [[0]]:
        return 0

    # Initializes variables
    rows = len(grid)
    cols = len(grid[0])
    bucket_capacity = capacity

    # Initializes arrays for the results
    max_fill = []
    filled = []
    filled_indexes = []

    # Main loop
    for row in range(rows):
        max_fill.append(0)
        filled.append(0)
        filled_indexes.append([])
        for col in range(cols):
            if grid[row][col] == 0:
                max_fill[row] += 1
            else:
                max_fill[row] += 2

    # Logic
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                continue
            if filled[row][col] == bucket_capacity:
                continue
            if filled[row][col] + 1 < bucket_capacity:
