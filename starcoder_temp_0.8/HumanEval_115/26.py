
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
    rows = len(grid)
    cols = len(grid[0])
    grid = [[0] + x + [0] for x in grid]
    grid = [[0] + grid[i] for i in range(len(grid))]
    for row in grid:
        row.append(0)
    max_fill = 0
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if grid[row][col] == 0:
                continue
            max_fill = max(
                max_fill,
                math.ceil((grid[row][col] + grid[row - 1][col]) / capacity)
                + math.ceil((grid[row][col] + grid[row][col - 1]) / capacity)
                - 1,
            )
    return max_fill
