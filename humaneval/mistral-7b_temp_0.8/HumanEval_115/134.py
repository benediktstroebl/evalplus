
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

    def helper(x, y, capacity):
        if (x, y) in visited:
            return
        if grid[x][y] == 0:
            return
        visited.add((x, y))
        if grid[x][y] <= capacity:
            return
        else:
            for i in range(4):
                if i == 0:
                    x -= 1
                if i == 1:
                    y += 1
                if i == 2:
                    x += 1
                if i == 3:
                    y -= 1
                helper(x, y, grid[x][y])
                x, y = ix[i], iy[i]

    ix = [0, 0, 1, 1]
    iy = [1, -1, 0, 0]
    visited = set()
    # if you find the wells empty return 0
    if all(all(cell == 0 for cell in row) for row in grid):
        return 0
