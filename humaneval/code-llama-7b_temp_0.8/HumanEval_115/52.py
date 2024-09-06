
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
    n_buckets, n_cols = len(grid), len(grid[0])
    n_fillings = sum([sum(row) for row in grid])
    if n_fillings < capacity:
        return 0
    if n_fillings == capacity:
        return math.floor(n_buckets / n_cols)

    # calculate number of empty buckets
    n_empty_buckets = n_buckets - n_fillings

    # calculate number of rows to be filled
    n_rows_to_fill = math.ceil(n_empty_buckets / n_cols)

    # calculate number of times to lower the buckets
    n_lowers = n_buckets - n_rows_to_fill * n_cols
    return n_lowers
