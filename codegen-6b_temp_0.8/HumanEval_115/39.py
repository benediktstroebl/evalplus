
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
    cols = len(grid[0])
    rows = len(grid)
    right_max_fill = [[0]*cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            right_max_fill[row][col] = grid[row][col]
            if col > 0:
                right_max_fill[row][col] = max(right_max_fill[row][col], grid[row][col-1])
            if row > 0:
                right_max_fill[row][col] = max(right_max_fill[row][col], grid[row-1][col])

    left_max_fill = [[0]*cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            left_max_fill[row][col] = grid[row][col]
            if col < cols-1:
                left_max_fill[row][col] = max(left_max_fill[row][col], grid[row][col+1])
            if row < rows-1:
                left_max_fill[row][col] = max(left_max_fill[row][col], grid[row+1][col])

    for row in range(rows):
        for col in range(cols):
            grid[row][col] = min(grid[row][col], right_max_fill[row][col], left_max_fill[row][col])

    total_water = sum([sum(g) for g in grid])
    return total_water - capacity

