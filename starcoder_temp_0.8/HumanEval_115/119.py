
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
    max_rows = len(grid)
    max_columns = len(grid[0])
    # create an empty 2D array
    lower_buckets = [[0 for _ in range(max_columns)] for _ in range(max_rows)]

    # going through each row
    for row_index, row in enumerate(grid):
        # going through each column
        for column_index, column in enumerate(row):
            # if the well is not empty
            if column == 1:
                # the maximum number of buckets we can use is the
                # minimum of the number of rows in the grid and the
                # number of columns in the grid
                max_buckets = min(row_index, max_columns)
                # calculate the minimum number of buckets we can
                # use to fill the well
                minimum_buckets = math.floor(column / capacity)
                # update the value of the cell in the array
                # to hold the maximum number of buckets we can use
                lower_buckets[row_index][column_index] = max(
                    max_buckets, minimum_buckets
                )
    # create a variable to hold the result
    result = 0
    # going through the 2D array
    for row in lower_buckets:
        # for each element in the row
        for element in row:
            # update the value of the variable
            result += element

    # return the result
    return result
