
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

    def find_max(grid, row):
        max_row = 0
        for i in range(len(grid[row])):
            if grid[row][i] == 1:
                max_row = i
        return max_row

    def find_min(grid, row):
        min_row = len(grid[row])
        for i in range(len(grid[row])):
            if grid[row][i] == 1:
                min_row = i
        return min_row

    def find_max_fill(grid, max_row):
        max_fill = 0
        for i in range(len(grid[0])):
            if grid[max_row][i] == 1:
                max_fill = i
        return max_fill

    def find_min_fill(grid, max_row, max_fill):
        for i in range(max_fill, len(grid[0])):
            if grid[max_row][i] == 1:
                return i

    def compare_row(row_index, row, min_row, min_fill
