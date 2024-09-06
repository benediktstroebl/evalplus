
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

    rows_fill = [math.inf] * rows
    cols_fill = [math.inf] * cols

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                rows_fill[r] = 0
                cols_fill[c] = 0

    counter = 0
    while True:
        counter += 1
        # rows
        for r in range(rows):
            prev = rows_fill[r]
            for c in range(cols):
                if grid[r][c] == 1 and cols_fill[c] < capacity:
                    rows_fill[r] += 1
                    cols_fill[c] += 1
                    break
            if prev == rows_fill[r]:
                break
        # cols
        for c in range(cols):
            prev = cols_fill[c]
            for r in range(rows):
                if grid[r][c] == 1 and rows_fill
