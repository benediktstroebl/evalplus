
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
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # def find_highest_column(grid, row):
    #     for col in range(len(grid[row])-1, -1, -1):
    #         if grid[row][col] == 1:
    #             return col
    #     return None
    #
    # def find_highest_column(grid, row):
    #     col = len(grid[row])-1
    #     while col > -1 and grid[row][col] == 0:
    #         col -= 1
    #     return col
    #
    # def find_highest_column(grid, row):
    #     for col in range(len(grid[row])):
    #         if grid[row][col] == 1:
    #             return col
    #     return None
    #
    # def find_highest_column(grid, row):
    #     col = 0
    #     while col < len(grid[row]) and grid[row][col] == 0:
    #         col += 1
    #     return col
    #
    # def fill_bucket(grid, capacity, row, col, times):
    #     print(grid)
    #     print(row, col, times)
    #     if col == len(grid[row])-1:
    #         times += 1
    #         row += 1
    #         col = 0
    #     else:
    #         if grid[row][col] == 1:
    #             capacity -= 1
    #             if capacity == 0:
    #                 times += 1
    #                 capacity = bucket_capacity
    #         else:
    #             if capacity < bucket_capacity:
    #                 times += 1
    #                 capacity = bucket_capacity
    #         col += 1
    #
    #     if row == len(grid)-1:
    #
