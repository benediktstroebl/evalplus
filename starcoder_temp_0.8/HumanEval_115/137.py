
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
    row_len = len(grid)
    col_len = len(grid[0])

    x_moves = [-1, 0, 1, 0]
    y_moves = [0, -1, 0, 1]

    bucket_fill_level = 0

    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                for k in range(4):
                    next_i = i + x_moves[k]
                    next_j = j + y_moves[k]

                    if (next_i >= 0 and next_i < row_len and next_j >= 0 and next_j < col_len):
                        grid[next_i][next_j] = 1

    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                bucket_fill_level = bucket_fill_level + 1

    full_count = math.ceil(bucket_fill_level / capacity)
    return full_count

