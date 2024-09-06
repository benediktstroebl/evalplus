import math
def max_fill(grid, capacity):
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
    # Calculate cumulative sum for each row (row_sum) and column (col_sum)
    row_sum = []
    col_sum = []
    for i in range(len(grid)):
        row = grid[i]
        current_sum = sum(row)
        row_sum.append(current_sum)
        col_sum.append(current_sum)
    for i in range(len(grid[0])):
        current_sum = sum(grid[j][i] for j in range(len(grid)))
        col_sum.append(current_sum)

    # Calculate the maximum number of dips for each row and column
    dips_row = [0] * len(grid)
    dips_col = [0] * len(grid[0])
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if row[j] == 1:
                dips_row[i] = max(dips_row[i], dips_col[j] + 1)
            else:
                dips_row[i] = max(dips_row[i], dips_col[j])
        dips_row[i] = max(dips_row[i], row_sum[i] // capacity)

    # Calculate total number of dips
    total_dips = sum(dips_row)
    return total_dips