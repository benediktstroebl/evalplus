
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
    n_rows, n_cols = len(grid), len(grid[0])
    if n_rows == 0:
        return 0
    count = 0
    max_level = []
    for i in range(n_cols):
        max_level.append(0)
        for j in range(n_rows):
            max_level[i] = max(max_level[i], grid[j][i])
    # print(max_level)
    min_level = [0] * n_cols
    for i in range(n_cols):
        min_level[i] = grid[n_rows-1][i]
    # print(min_level)
    for i in range(n_rows - 2, -1, -1):
        for j in range(n_cols):
            min_level[j] = min(min_level[j], grid[i][j])
    # print(min_level)
    for i in range(n_cols):
        diff = (max_level[i] - min_level[i]) / capacity
        if diff > 0:
            count += math.ceil(diff)
    # print(count)
    return count
