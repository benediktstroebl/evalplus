
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
    # grid = [
    #     [0,0,1,0],
    #     [0,1,0,0],
    #     [1,1,1,1]
    # ]
    # capacity = 1
    rows = len(grid)
    cols = len(grid[0])
    max_area = capacity * rows
    buckets = [i for i in range(cols)]

    def fill(i, j, area):
        if area > max_area or j >= cols or i >= rows or grid[i][j] == 0:
            return 0
        area += 1
        grid[i][j] = 0
        return 1 + fill(i + 1, j, area) + fill(i, j + 1, area) + fill(i - 1, j, area) + fill(i, j - 1, area)

    max_fill = 0
    for bucket in buckets:
        for i in range(rows):
            for j in range(cols):
                max_fill = max(max_fill, fill(i, bucket, 0))
    return max_fill

