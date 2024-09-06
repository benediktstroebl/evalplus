
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

    max_water_left = [[0 for i in range(cols)] for j in range(rows)]

    # store the max water that can be stored from a cell
    # it's either the water in the cell itself, or the max capacity
    # whichever is greater
    for row in range(rows):
        for col in range(cols):
            left_max = max(grid[row][col], capacity)
            if col + 1 < cols:
                left_max = max(left_max, max_water_left[row][col + 1])
            max_water_left[row][col] = left_max

    # store the max water that can be stored from a cell
    # it's either the water in the cell itself, or the max capacity
    # whichever is greater
    for row in reversed(range(rows)):
        for col in reversed(range(cols)):
            top_max = max(grid[row][col], capacity)
            if row + 1 < rows:
                top_max = max(top_max, max_water_left[row + 1][col])
            max_water_left[row][col] = min(max_water_left[row][col], top_max)

    return math.ceil(sum(max_water_left[i][j] for i in range(rows) for j in range(cols)))

