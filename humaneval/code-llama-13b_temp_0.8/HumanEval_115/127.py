
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
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    while True:
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # Left
                    if col > 0:
                        if grid[row][col] == 1 and grid[row][col - 1] == 0:
                            grid[row][col - 1] = 1
                            count += 1
                    # Right
                    if col < cols - 1:
                        if grid[row][col] == 1 and grid[row][col + 1] == 0:
                            grid[row][col + 1] = 1
                            count += 1
                    # Up
                    if row > 0:
                        if grid[row][col] == 1 and grid[row - 1][col] == 0:
                            grid[row - 1][col] = 1
                            count += 1
                    # Down
                    if row < rows - 1:
                        if grid[row][col] == 1 and grid[row + 1][col] == 0:
                            grid[row + 1][col] = 1
                            count += 1
        if any(1 in row for row in grid):
            return count
        else:
            return 0
    
