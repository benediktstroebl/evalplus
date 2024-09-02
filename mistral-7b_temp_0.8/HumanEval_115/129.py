
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
    row_len = len(grid)
    col_len = len(grid[0])

    bucket = capacity
    min_dist = math.inf
    max_fill = 0

    # 4 directions
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # check for each cell to find max fill
    for row in range(row_len):
        for col in range(col_len):
            if grid[row][col] == 1:
                temp_max_fill = 0
                temp_min_dist = 0
                for direction in directions:
                    curr_row = row
                    curr_col = col
                    while curr_row >= 0 and curr_row < row_len and curr_col >= 0 and curr_col < col_len:
                        if grid[curr_row][curr_col] == 1:
                            break
                        if grid[curr_row][curr_col] == 0:
                            temp_max_fill += 
