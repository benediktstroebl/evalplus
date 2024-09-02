
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
    import copy
    row_len = len(grid)
    col_len = len(grid[0])
    cur_row_idx = 0
    cur_row_max_idx = 0
    steps = 0
    while True:
        check_row = True
        for i in range(row_len):
            if grid[i][cur_row_idx] == 1:
                if check_row:
                    cur_row_idx += 1
                else:
                    check_row = False
        if check_row:
            break
        steps += 1
    
    cur_col_idx = 0
    len_row = math.floor(capacity / row_len)
    while True:
        check_col = True
        for i in range(col_len):
            if grid[cur_row_idx][i] == 1:
                if check_col:
                    cur_col_idx += 1
                else:
                    check_col = False
        if check_col:
            break
        steps += 1
    
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == 1:
                grid[i][j] = 0
    
    if len_row > 1:
        for row in range(row_len):
            prev_row = copy.deepcopy(grid[row])
            for i in range(len_row):
                grid[row][i] = 1
            while True:
                check_row = True
                for i in range(row_len):
                    if grid[i][0] == 1:
                        if check_row:
                            prev_row[0] = 1
                        else:
                            check_row = False
                if check_row:
                    break
                steps += 1
            for i in range(len_row):
                grid[row][i] = 0
        steps += 1
    
    if len_row > 1:
        for col in range(col_len):
            prev_col = copy.deepcopy(grid[0])
            for i in range(len_row):
                grid[i][col] = 1