
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
    row, col = grid[0].index(0)
    bucket_list = [grid[row:row+1, col:col+1].index(0) for _ in grid]
    bucket_index = [0] * (max(row+1, col+1) // (1 if grid[row][col] == 1 else bucket_capacity) + 1)
    bucket_index = bucket_index[:, :] = grid[0][:, :]
    max_len = max([len(row) for row in grid])
    for i in range(max_len):
        bucket_index[0][i] = i
        for j in range(1, max_len + 1):
            for k, v in zip(bucket_index[0][:, j:], bucket_list):
                if v == i:
                    bucket_index[j][k] = i
    max_fill_count = 0
    for j in range(max_len):
        for i in range(1, max_len + 1):
            if bucket_index[j][i] == 0:
                bucket_index[j][i] = max_fill_count
                max_fill_count += 1
    return max_fill_count
