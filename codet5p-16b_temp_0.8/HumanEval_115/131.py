
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

    rows = len(grid)
    columns = len(grid[0])
    if columns == 0: return 0
    rows_list = list()
    columns_list = list()
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                rows_list.append(row)
                columns_list.append(column)
    rows_list.sort()
    columns_list.sort()
    if len(rows_list) == 0: return 0
    if len(rows_list) == 1: return 0
    if len(rows_list) == 2: return math.ceil((rows_list[1] - rows_list[0]) / 2)
    if len(rows_list) == 3: return math.ceil((rows_list[2] - rows_list[1]) / 2)
    return math.ceil((rows_list[-1] - rows_list[-2]) / 2) + math.ceil((columns_list[-1] - columns_list[-2
