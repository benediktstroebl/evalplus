
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
    m, n = len(grid), len(grid[0])
    max_elements = sum(grid[i][j] for i in range(m) for j in range(n))
    if max_elements <= capacity:
        return 0

    min_capacity_to_fill = max_elements // capacity + 1
    capacity_to_fill = max_elements // min_capacity_to_fill
    buckets_needed = max_elements // capacity_to_fill

    buckets_filled = 0
    row_sum = 0
    col_sum = [0] * n
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                row_sum += 1
                col_sum[j] += 1
            if row_sum == capacity:
                row_sum = 0
                buckets_filled += 1
            if col_sum[j] == capacity:
                col_sum[j] = 0
                buckets_filled += 1
    
    return buckets_filled

