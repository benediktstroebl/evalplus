
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
    # Solution
    max_water_capacity, rows_len = 0, len(grid)
    for row in grid:
        max_water_capacity += max(row)
    if max_water_capacity == 0:
        return 0
    # first row:
    #   are the only rows where the buckets can be used
    #   we can't use the bucket in row 0
    #   we need to lower the buckets in row 0
    #   we can't use the bucket in row n
    #   we need to lower the buckets in row n
    # first column:
    #   we can't use the bucket in column 0
    #   we can't use the bucket in column n
    # all other columns
    #   we can use the bucket in column 1...n-1
    #   we can't use the bucket in column 0
    #   we need to lower the buckets in column 0...n-1
    #   we can't use the bucket in column n
    #   we need to lower the buckets in column n
    # water can be captured in each column of each row
    #   water captured = min(bucket_capacity, max(row))
    # total water captured = min(bucket_capacity, max(row)) * (rows_len - 1)
    #   no water captured in 1st row
    #   water captured in 2nd row = min(bucket_capacity, max(row))
    #   water captured in 3rd row = min(bucket_capacity, max(row)) * 2
    #   water captured in 4th row = min(bucket_capacity, max(row)) * 3
    #   ...
    #   water captured in nth row = min(bucket_capacity, max(row)) * (rows_len - 1)
    #   total water captured = 
    #       sum(water captured in all rows) = 
    #       sum(min(bucket_capacity, max(row)) * (rows_len - 1)) = 
    #       min(bucket_capacity, max(row)) * rows_len *
