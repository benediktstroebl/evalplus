
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
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    # Create buckets and refilled buckets in a grid
    buckets = [[0]*(grid_cols) for _ in range(grid_rows)]
    for row in range(grid_rows):
        for col in range(grid_cols):
            if grid[row][col] == 1:
                buckets[row][col] = capacity
    # Count the number of times we need to refill the buckets
    result = 0
    for row in range(grid_rows):
        for col in range(grid_cols):
            for x in range(grid_rows):
                if buckets[x][col] > 0:
                    buckets[x][col] -= 1
            result += 1
    return result

inputs = [[[0,0,1,0], [0,1,0,0], [1,1,1,1]], [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], [[0,0,0], [0,0,0]], [[0,0,0], [0,0,0]]]
expected_outputs = [6, 5, 0, 0]
