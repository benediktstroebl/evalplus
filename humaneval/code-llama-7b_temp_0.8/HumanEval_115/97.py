
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
    # find all the 1's in the grid
    # sort them from left to right (or top to bottom)
    # iterate through each 1 and see how many 1's it can reach with a certain capacity
    # return the number of times the bucket needs to be lowered

    total_ones = 0
    total_buckets = 0
    for row in grid:
        total_ones += row.count(1)
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if row[j] == 1:
                total_buckets += 1
    
    # if no 1's then no lowering needed
    if total_buckets == 0:
        return 0
    # if one well, no lowering needed
    if total_ones == 1:
        return 1
    
    lower_times = 1
    # need to do a few things
    # count the 1's in the first row,
    # count the 1's in the 2nd row,
    # count the 1's in the 3rd row, etc.
    # count the 1's in the first column,
    # count the 1's in the 2nd column,
    # count the 1's in the 3rd column, etc.

    # count the 1's in the first row
    total_ones_row_col = 0
    total_buckets_row_col = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if i == 0 and j == 0:
                total_ones_row_col += row[j]
                total_buckets_row_col += 1 if row[j] == 1 else 0
            elif i == 0:
                total_ones_row_col += row[j]
                total_buckets_row_col += 1 if row[j] == 1 else 0
            elif j == 0:
                total_ones_row_col += grid[j
