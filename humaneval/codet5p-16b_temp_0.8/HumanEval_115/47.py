
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

    bucket_count = 0
    bucket_buckets = 0
    row_count = len(grid)
    col_count = len(grid[0])

    def bucket_fill(grid, row, col, buckets):
        from math import ceil
        bucket_buckets = buckets
        current_well = grid[row][col]

        if current_well == 0:
            return bucket_buckets

        bucket_buckets += ceil(current_well / bucket_capacity)
        grid[row][col] = 0
        return bucket_fill(grid, row - 1, col, bucket_buckets)

    def bucket_empty(grid, row, col, buckets):
        from math import ceil
        bucket_buckets = buckets
        current_well = grid[row][col]

        if current_well == 0:
            return bucket_buckets

        bucket_buckets += ceil(current_well / bucket_capacity)
        grid[row][col] = 0
        return bucket_empty(grid, row + 1, col, bucket_buckets)

    
