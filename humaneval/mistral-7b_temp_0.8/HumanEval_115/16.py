
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

    def get_num_times_to_empty(grid, bucket_capacity):
        rows = len(grid)
        cols = len(grid[0])
        num_times = 0
        while True:
            # get the first non-empty column
            column_num = None
            for i in range(rows):
                if grid[i][0] == 1:
                    column_num = 0
                    break
            if column_num == None:
                return num_times
            # iterate through the column and empty the wells
            for i in range(rows):
                if grid[i][column_num] == 1:
                    if bucket_capacity >= grid[i][column_num]:
                        grid[i][column_num] = 0
                        num_times += 1
                    else:
                        break
        return num_times

    # if there is only one non-empty cell, return 1
    num_times = 0
    for i in range(rows):
        for j in range(cols):
