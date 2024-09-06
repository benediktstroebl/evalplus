
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
    n = len(grid)
    m = len(grid[0])

    # Check if the grid is completely empty
    if grid == [[0 for _ in range(n)] for _ in range(m)]:
        return 0

    # Initialize the number of times to lower the buckets
    times = 0

    # Place the buckets in the grid
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                if not grid[i-1][j]:
                    grid[i][j] = 0
                if not grid[i+1][j]:
                    grid[i][j] = 0
                if not grid[i][j-1]:
                    grid[i][j] = 0
                if not grid[i][j+1]:
                    grid[i][j] = 0

    # Drain the buckets
    while not all(grid == [[0] * n for _ in range(m)] for _ in range(n)):
        times += 1
        if times == grid[0][0]:
            return grid.index(grid[0][0])
        for i in range(n-1):
            for j in range(m):
                if grid[i][j] == 1:
                    if not grid[i+1][j]:
                        grid[i][j] = 0
                        break
                    elif grid[i+1][j] == 1:
                        grid[i+1][j] = 0
                        grid[i][j] = 0
                        break
                    else:
                        grid[i][j] = 0
    return 0