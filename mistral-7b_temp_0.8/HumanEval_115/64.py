
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
    grid = [list(x) for x in grid]
    max_height = 0
    for row in grid:
        if max_height < max(row):
            max_height = max(row)

    # create a sorted list of all the heights of the wells from highest to lowest
    # the index of the sorted list is the row number
    max_height_list = sorted(max_height)

    # create a dictionary of max_height_list and the row that corresponds to it
    # e.g. {1:1, 2:2, 3:1, 4:2, 5:1, 6:1, 7:2, 8:1}
    # {height: row}
    max_height_rows = {x:i for i, x in enumerate(max_height_list)}

    # initialize empty array that will hold the max height of each row, starting at row 1
    height_row_count = [0] * (max_height + 1)

    # initialize the number of times we need to lower the bucket to
