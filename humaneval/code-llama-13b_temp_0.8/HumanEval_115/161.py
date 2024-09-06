
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
    if not grid:
        return 0

    width = len(grid[0])
    height = len(grid)
    bucket_count = capacity
    fill_count = 0

    def fill_from(x, y):
        nonlocal bucket_count
        if x < 0 or x >= width or y < 0 or y >= height:
            return False
        if grid[y][x] == 0:
            return False
        if grid[y][x] == 1:
            grid[y][x] = 0
            bucket_count -= 1
        return True

    for x in range(width - 1, 0, -1):
        if bucket_count == 0:
            break
        for y in range(height - 1, 0, -1):
            fill_from(x, y)
            if bucket_count == 0:
                break
        if bucket_count > 0:
            fill_count += 1
        for y in range(0, height):
            fill_from(x, y)
            if bucket_count == 0:
                break
        if bucket_count > 0:
            fill_count += 1

    return fill_count
