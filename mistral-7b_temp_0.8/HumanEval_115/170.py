
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
    def can_fill(row, col):
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        return grid[row][col]

    def fill_bucket(row, col, capacity, grid, bucket_capacity):
        """
        Fill the bucket with water from the well at (row, col).
        """
        if not can_fill(row, col):
            return False
        if grid[row][col] >= bucket_capacity:
            grid[row][col] -= bucket_capacity
            return True
        else:
            return False

    def fill_bucket_row(row, capacity, grid, bucket_capacity):
        """
        Fill the bucket with water from the wells on the row at row.
        """
        fill_count = 0
        for col in range(len(grid[0])):
            if fill_bucket(row, col, capacity, grid, bucket_capacity):
                fill_count += 1
        return fill_count

    
