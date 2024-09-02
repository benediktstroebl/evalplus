
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
    if grid is None or len(grid) == 0:
        return 0
    if isinstance(grid[0], list):
        grid = transpose(grid)
    total_capacity = sum(row.count(1) for row in grid)

    import math
    number_of_columns = len(grid)
    number_of_rows = len(grid[0])
    bucket_per_row = int((math.ceil(capacity / number_of_columns)))
    row_bucket_capacity = bucket_per_row * number_of_columns
    if row_bucket_capacity > capacity:
        row_bucket_capacity = capacity

    row_buckets = [[0 for _ in range(row_bucket_capacity)] for _ in range(number_of_rows)]
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if column:
                row_buckets[row_index][column_index] += 1
    total_buckets = sum(row.count(1) for row in row_buckets)
    for row_index, row in enumerate(row_buckets):
        if row.count(1) > bucket_per_row:
            total_buckets -= row.count(1) - bucket_per_row

    return total_buckets
