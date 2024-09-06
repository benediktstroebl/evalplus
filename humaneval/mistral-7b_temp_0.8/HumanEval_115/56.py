
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
    # create a dictionary for each row
    # for each row, count the number of 1s
    # for each row, use the capacity to fill the row
    # count the number of rows that can be filled
    # count the number of buckets needed
    # return number of buckets

    # iterate over each row
    # keep track of number of 1s in each row
    # return maximum number of 1s that can be filled with capacity
    row_count = len(grid)
    col_count = len(grid[0])

    # create a dictionary for each row
    row_dict = {}
    for i in range(row_count):
        row_dict[i] = {}

    # iterate over each row
    for i in range(row_count):
        row_1_count = 0
        for j in range(col_count):
            if grid[i][j] == 1:
                row_1_count += 1
            else:
                pass
        row_dict[i]["capacity"] = row_1_count
