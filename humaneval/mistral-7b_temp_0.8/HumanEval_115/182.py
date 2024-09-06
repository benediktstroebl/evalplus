
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
    def min_buckets(grid, capacity):
        """ Returns the minimum number of buckets needed to empty all wells """
        dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(grid))]
        for i in range(len(grid)):
            dp[i][0] = 0
        return dp_fill(grid, capacity, 0, 0, dp)

    def dp_fill(grid, capacity, i, j, dp):
        """
        Recursive function to find the minimum number of buckets needed
        to empty the wells in the grid.

        Returns: The minimum number of buckets needed to empty all wells.
        """
        # Base case: if i is out of bounds or the grid is empty, return 0
        if i == len(grid) or j == len(grid[0]):
            return 0

        # Recursive case: check if the grid cell at (i, j) is empty
        if grid[i][j] == 1:
            # If it is empty, add 1
