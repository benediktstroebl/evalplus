
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
    # def fill_bucket(row, column):
    #     if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
    #         return
    #     if grid[row][column] == 0:
    #         return
    #     grid[row][column] = 0
    #     fill_bucket(row-1, column)
    #     fill_bucket(row+1, column)
    #     fill_bucket(row, column-1)
    #     fill_bucket(row, column+1)
    
    # number_of_times = 0
    # for row in range(len(grid)):
    #     for column in range(len(grid[0])):
    #         if grid[row][column] == 1:
    #             fill_bucket(row, column)
    #             number_of_times += 1

    # return number_of_times

    # Version 2
    def fill_bucket(row, column):
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
            return math.inf, math.inf
        if grid[row][column] == 0:
            return math.inf, math.inf
        return row, column
    
    number_of_times = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 1:
                row, column = fill_bucket(row, column)
                while row != math.inf and column != math.inf:
                    row, column = fill_bucket(row-1, column)
                    row, column = fill_bucket(row+1, column)
                    row, column = fill_bucket(row, column-1)
                    row, column = fill_bucket(row, column+1)
                number_of_times += 1
    return number_of_times
