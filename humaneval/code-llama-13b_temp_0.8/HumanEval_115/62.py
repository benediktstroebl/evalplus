
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
    # def fill_left(i, j):
    #     if i < 0 or j < 0:
    #         return 0
    #     elif grid[i][j] == 1:
    #         return fill_left(i, j-1) + 1
    #     else:
    #         return fill_left(i, j-1)
    
    # def fill_right(i, j):
    #     if i < 0 or j >= len(grid[0]):
    #         return 0
    #     elif grid[i][j] == 1:
    #         return fill_right(i, j+1) + 1
    #     else:
    #         return fill_right(i, j+1)

    # def fill_up(i, j):
    #     if i < 0 or j < 0 or j >= len(grid[0]):
    #         return 0
    #     elif grid[i][j] == 1:
    #         return fill_up(i-1, j) + 1
    #     else:
    #         return fill_up(i-1, j)

    # def fill_down(i, j):
    #     if i >= len(grid) or j < 0 or j >= len(grid[0]):
    #         return 0
    #     elif grid[i][j] == 1:
    #         return fill_down(i+1, j) + 1
    #     else:
    #         return fill_down(i+1, j)
    
    # fills = []
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1:
    #             fills.append(max(fill_left(i, j), fill_right(i, j), fill_up(i, j), fill_down(i, j)))
    #         else:
    #             fills.append(0)
    
    # result = 0
    # for i in range(0, len(fills),
