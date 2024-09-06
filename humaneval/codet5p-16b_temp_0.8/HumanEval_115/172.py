
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

    bucket_size = capacity

    def left(grid, row, col):
        if col-1 >= 0 and grid[row][col-1] == 1:
            return bucket_size

        return 0

    def right(grid, row, col):
        if col+1 < len(grid[0]) and grid[row][col+1] == 1:
            return bucket_size

        return 0

    def top(grid, row, col):
        if row-1 >= 0 and grid[row-1][col] == 1:
            return bucket_size

        return 0

    def bottom(grid, row, col):
        if row+1 < len(grid) and grid[row+1][col] == 1:
            return bucket_size

        return 0

    def fill(grid, row, col, bucket_size):
        grid[row][col] = bucket_size

        bucket_size -= 1

        if row-1 >= 0 and grid[row-1][col] == 1:
            fill(grid, row-1, col, bucket_size)

        if row+1
