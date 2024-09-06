
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

    def row_size(grid):
        """
        Return the size of a given row
        """
        return len(grid[0])

    def max_fill(grid, bucket_capacity):
        """
        Returns the number of times you need to lower the buckets to empty the wells
        """

        # Find the max number of buckets needed for a row
        n = min([bucket_capacity, max([grid[i][:row_size(grid)] for i in range(len(grid))])])

        # Check if we need to fill the bucket
        if n <= bucket_capacity:
            return max_fill(grid, n)

        # Find the number of times we need to lower the buckets
        counter = 0
        for i in range(len(grid)):
            while grid[i][:row_size(grid)] > 0:
                grid[i] = grid[i][1:]
                counter += 1

        return counter
