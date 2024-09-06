
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

    def is_empty(row, col):
        return grid[row][col] == 0

    def add_to_bucket(row, col):
        """
        Assumes the bucket is empty
        """
        if is_empty(row, col):
            grid[row][col] = 1
            return True
        return False

    def is_full(row, col):
        return grid[row][col] == capacity

    def empty_bucket(row, col):
        """
        Assumes the bucket is full
        """
        if is_full(row, col):
            grid[row][col] = 0
            return True
        return False

    def move_bucket(row, col, capacity):
        """
        Adds capacity units to row, col
        Removes capacity units from row, col
        Assumes that the bucket is empty or full
        """
        if is_empty(row, col):
            grid[row][col] = capacity
            return True
        if is_full(row, col):
            grid[row][col] =
