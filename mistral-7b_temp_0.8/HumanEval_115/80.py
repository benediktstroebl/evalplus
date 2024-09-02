
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

    def max_fill_rec(grid, capacity, row, col, fill):
        # base case
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 0:
            return 0

        if grid[row][col] > capacity:
            return 0

        # if we have filled the grid, return the number of times we have filled the grid
        if fill == (len(grid) * len(grid[0])):
            return 1

        # fill the grid and return 1 more time
        grid[row][col] -= capacity
        fill += 1

        # fill the grid in all possible directions
        return max_fill_rec(grid, capacity, row - 1, col, fill) + max_fill_rec(grid, capacity, row, col + 1, fill) + max_fill_rec(grid, capacity, row + 1, col, fill) + max_fill_rec(grid, capacity, row, col - 1, fill)


    
