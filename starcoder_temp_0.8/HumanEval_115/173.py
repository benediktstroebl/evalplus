
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
    # Time: O(wh)
    # Space: O(wh)
    n, m = len(grid), len(grid[0])
    # for every well, a max_row will help maximize the water
    # flow to the left
    max_row = [0] * n
    # for every well, a max_col will help maximize the water
    # flow downward
    max_col = [0] * m
    for row in range(n):
        for col in range(m):
            max_row[row] = max_row[row] if grid[row][col] == 0 else max_row[row] + 1
            max_col[col] = max_col[col] if grid[row][col] == 0 else max_col[col] + 1
    # each well's max flow downward is at least the max flow
    # right
    # for every well, a min_col will help minimize the water
    # flow downward
    min_col = [max_col[col] for col in range(m)]
    for row in range(n-1, -1, -1):
        for col in range(m-1, -1, -1):
            min_col[col] = min(min_col[col], max_row[row])
            if grid[row][col] == 0:
                max_row[row] = max_row[row] - 1
    # flow downward
    # for every well, a min_col will help minimize the water
    # flow upward
    min_col = [min_col[col] for col in range(m)]
    for row in range(n-1, -1, -1):
        for col in range(m-1, -1, -1):
            min_col[col] = min(min_col[col], max_row[row])
            if grid[row][col] == 0:
                max_row[row] = max_row[row] - 1
    # flow upward
    # use min_col to calculate how many times we need to lower
    # buckets
    return math.ceil(sum(min_col) / capacity)
