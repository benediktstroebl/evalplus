
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

    def count_neighbours(row, col):
        """
        Count the number of 1s that are neighbours of (row, col).
        """
        count = 0
        if row > 0:
            count += grid[row-1][col]
        if col > 0:
            count += grid[row][col-1]
        if row < n-1:
            count += grid[row+1][col]
        if col < n-1:
            count += grid[row][col+1]
        return count

    def fill_bucket(row, col):
        """
        Fill the bucket with water at (row, col).
        """
        bucket = 0
        while bucket < capacity and count_neighbours(row, col) > 0:
            bucket += 1
            grid[row][col] = 0

    def extract_water(row, col):
        """
        Extract water from the bucket at (row, col).
        """
        grid[row][col] = 1
        return bucket

