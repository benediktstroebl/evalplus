
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
    # return 0
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1),
    ]
    n_steps = 0
    # start with a bucket position at the bottom right corner
    x, y = rows - 1, cols - 1
    # only check wells with water inside
    wells = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] > 0:
                wells.append((i, j))
    # for each bucket position, check all wells if they are fillable
    while len(wells) > 0:
        x, y = wells.pop()
        for direction in directions:
            dx, dy = direction
            while (x + dx >= 0 and x + dx < rows and y + dy >= 0 and y + dy < cols and grid[x + dx][y + dy] > 0) or (x + dx < 0 or x + dx >= rows or y + dy < 0 or y + dy >= cols):
                x += dx
                y += dy
            if grid[x][y] > 0:
                n_steps += 1
                grid[x][y] -= 1
                wells.append((x, y))
    return n_steps
