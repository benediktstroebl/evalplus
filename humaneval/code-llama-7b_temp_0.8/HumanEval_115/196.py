
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
    # We will first consider the cases where the grid is all zero.
    # Then, we will consider the cases where at least one well has a non-zero unit.
    if all(all(row == 0 for row in grid)):
        return 0
    else:
        # For each row that has a non-zero unit, we will find the maximum number of non-zero units
        # that can be covered in one row.
        # For instance, if the first row has 2 non-zero units, the second row has 3 non-zero units, and the
        # third row has 1 non-zero unit, then the maximum number of non-zero units that can be covered in one
        # row is 3. 
        max_coverage = 0
        row_count = len(grid)
        col_count = len(grid[0])
        for row in grid:
            max_coverage = max(max_coverage, row.count(1))
        # The total number of times we can lower a bucket is equal to the total number of times
        # we need to lower a bucket in one row times the number of rows.
        total_times = max_coverage * row_count
        # The total number of times we can lower a bucket is also equal to the total number of times
        # we need to lower a bucket in one row times the number of rows, divided by the capacity of a bucket.
        # This is because for any row, we need to calculate how many buckets we can use to cover as many units as
        # possible in that row.
        # For instance, if the first row can be covered by two buckets, the second row can be covered by three buckets,
        # and the third row can be covered by one buckets, then we will need 2 + 3 + 1 / 1 = 6 buckets to cover the
        # maximum number of non-zero units in each row.
        # total_times = max_coverage * row_count
        # total_times = math.ceil(total_times / capacity)
        return total_times
