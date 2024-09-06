
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

    def bucket_fill(grid, capacity):
        grid_len = len(grid)
        if grid_len == 0:
            return 0
        row_len = len(grid[0])
        if row_len == 0:
            return 0
        bucket_len = len(grid[0][0])
        if bucket_len == 0:
            return 0
        buckets = [ [ [] for _ in range(bucket_len) ] for _ in range(row_len) ]
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                for i in range(bucket_len):
                    buckets[row_idx][col_idx].append(0)

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                for i in range(row_len):
                    buckets[i][col_idx][col] += 1

        def bucket_capacity_calculation(bucket, capacity):
            calculated_bucket =
