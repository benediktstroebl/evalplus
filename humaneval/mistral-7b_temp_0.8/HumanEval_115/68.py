
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
    if capacity < 1 or capacity > 10:
        raise ValueError("Capacity must be between 1 and 10")
    if len(grid) == 0 or len(grid[0]) == 0:
        raise ValueError("Grid must have at least one row and one column")
    if any(len(row) < 1 for row in grid):
        raise ValueError("Grid must have at least one row and one column")
    if any(len(row) > 100 for row in grid):
        raise ValueError("Grid must have at most 100 columns")
    if any(len(row) > 100 for row in grid):
        raise ValueError("Grid must have at most 100 rows")
    if any(any(1 > cell > 2 for cell in row) for row in grid):
        raise ValueError("Grid cells must be 0 or 1")

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # using BFS to get number of steps
    queue = []
    for r
