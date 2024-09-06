
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
    def fill(grid, r, c, capacity, d, cost):
        # fill the bucket
        for i in range(r, r+d):
            for j in range(c, c+d):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    capacity -= 1
                    if capacity == 0: return True, cost
        # move bucket to the right
        if r+d < len(grid):
            for j in range(c, c+d):
                if grid[r+d][j] == 1:
                    grid[r+d][j] = 0
                    capacity -= 1
                    if capacity == 0: return True, cost + 1
        # move bucket to the bottom
        if c+d < len(grid[0]):
            for i in range(r, r+d):
                if grid[i][c+d] == 1:
                    grid[i][c+d] = 0
                    capacity -= 1
                    if capacity == 0: return True, cost + 1
        # move bucket to the left
        if c+d < len(grid[0]):
            for i in range(r, r+d):
                if grid[i][c+d] == 1:
                    grid[i][c+d] = 0
                    capacity -= 1
                    if capacity == 0: return True, cost + 1
        return False, cost

    # find the maximum fill size
    max_d = min(len(grid), len(grid[0]))
    max_d = min(max_d, capacity)
    # iterate over all fill sizes
    for d in range(1, max_d + 1):
        # iterate over all starting points in the grid
        for r in range(len(grid) - d + 1):
            for c in range(len(grid[0]) - d + 1):
                # if the bucket has been filled
                if grid[r][c] == 0: continue
                # fill the bucket
                filled, cost = fill(grid, r, c,
