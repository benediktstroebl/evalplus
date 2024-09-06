
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
    area = 0
    # count the amount of ones in the grid
    for row in grid:
        area += sum(row)
    # calculate the amount of times the bucket can fill the grid
    times_bucket_can_fill = area//capacity
    print(times_bucket_can_fill)
    # this is the rows that will fill
    rows_to_fill = grid[:times_bucket_can_fill]
    # this is the rows that will be left behind
    rows_to_not_fill = grid[times_bucket_can_fill:]
    # this is the columns that will fill
    columns_to_fill = []
    # this is the columns that will be left behind
    columns_to_not_fill = []
    # now we count the columns that have to fill
    for column in range(len(rows_to_fill[0])):
        area = sum([row[column] for row in rows_to_fill])
        if area != 0:
            columns_to_fill.append(column)
        else:
            columns_to_not_fill.append(column)

    # now we count the columns that have to not fill
    for column in range(len(rows_to_not_fill[0])):
        area = sum([row[column] for row in rows_to_not_fill])
        if area != 0:
            columns_to_not_fill.append(column)
        else:
            columns_to_fill.append(column)

    print(columns_to_fill)
    print(columns_to_not_fill)

    # now we have to count the number of rows
    # that have to fill and that don't fill
    rows_to_fill = []
    rows_to_not_fill = []
    for row in range(len(grid)):
        if sum(grid[row]) != 0:
            rows_to_fill.append(row)
        else:
            rows_to_not_fill.append(row)

    # now we have to find the total number of fills and empties
    number_of_fills = 0
    number_of_empt
