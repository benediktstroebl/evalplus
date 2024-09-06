
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
    # Your code here
    def get_num_buckets(grid, capcity):
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_buckets = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] > 0:
                    num_buckets += 1
        return num_buckets

    def get_num_buckets_taken_empty(grid, capcity):
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_buckets_taken_empty = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] > 0:
                    num_buckets_taken_empty += 1
        return num_buckets_taken_empty

    def get_num_buckets_empty(grid, capcity):
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_buckets_empty = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    num_buckets_empty += 1
        return num_buckets_empty

    def get_lowest_bucket_row(grid, capcity):
        num_rows = len(grid)
        num_cols = len(grid[0])
        lowest_bucket_row = num_rows
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] > 0:
                    lowest_bucket_row = i
                    break
        return lowest_bucket_row

    def get_lowest_bucket_col(grid, capcity):
        num_rows = len(grid)
        num_cols = len(grid[0])
        lowest_bucket_col = num_cols
        for j in range(num_cols):
            for i in range(num_rows):
               
