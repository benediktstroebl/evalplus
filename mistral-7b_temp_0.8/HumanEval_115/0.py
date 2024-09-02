
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

    def is_within_boundaries(x, y):
        """
        checks if (x,y) is within the bounds of the grid
        """
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def extract_water(x, y, grid, capacity):
        """
        extracts water from the specified well
        """
        if is_within_boundaries(x, y) and grid[x][y] == 1:
            grid[x][y] -= 1
            return True
        return False

    def fill_bucket(x, y, grid, capacity):
        """
        fills the bucket with water from the specified well
        """
        if not is_within_boundaries(x, y):
            return False
        return extract_water(x, y, grid, capacity)

    def extract_water_from_well(x, y, grid, capacity):
        """
        extracts water from the specified well until the bucket is full or the well is empty
        """
        if is_
