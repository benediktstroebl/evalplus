
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
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    def count_tiles(row, col):
        """
        Return the number of tiles that we need to fill.
        """
        res = 0
        while grid[row][col] == 1:
            res += 1
            if row < rows-1: row += 1
            else: break
        return res
    def dp(row, col, filled):
        """
        Get the minimum number of buckets needed to fill all the tiles of
        the grid starting from (row, col) and ending at (row, col).

        Each step, we can do two things:
        * Try to fill the current cell
        * Try to go to the adjacent cell
        """
        # Check if we have reached the end of the grid
        if row >= rows or col >= cols: return 0
        # Check if the cell has already been filled
        if filled[row][col]: return 0
        # Mark the cell as filled
        filled[row][col] = True
