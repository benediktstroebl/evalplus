
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
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_buckets = int(math.floor(capacity + num_cols))
    row_indices = []
    for i in range(num_rows):
        for j in range(num_cols):
            grid[i][j] *= 1000
    for i in range(num_rows):
        row_sum = sum(grid[i])
        if row_sum > capacity:
            row_indices.append(i)
    for i in row_indices:
        row_sum = sum(grid[i])
        bucket_indices = []
        for j in range(num_cols):
            if grid[i][j] > capacity:
                bucket_indices.append(j)
        for j in bucket_indices:
            bucket_sum = grid[i][j]
            bucket_num = int(bucket_sum / capacity)
            for k in range(bucket_num):
                for l in range(num_rows):
                    grid[l][j] -= capacity
            if bucket_sum % capacity != 0:
                for l in range(num_rows):
                    grid[l][j] -= (bucket_sum % capacity)
        row_sum = sum(grid[i])
        bucket_num = int(row_sum / capacity)
        for k in range(bucket_num):
            for l in range(num_cols):
                grid[i][l] -= capacity
        if row_sum % capacity != 0:
            for l in range(num_cols):
                grid[i][l] -= (row_sum % capacity)
    num_fills = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] > capacity:
                num_fills += int(grid[i][j] / capacity)
            elif grid[i][j] > 0:
                num_fills += 1
    return num_fills

