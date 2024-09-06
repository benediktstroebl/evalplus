
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
    import math

    def extract_water(row):
        """
        How many times it is possible to extract water from the row

        Args:
            row (list): list of 0s and 1s
        Returns:
            int: number of times you can extract water from the row
        """
        if len(row) == 0:
            return 0
        # initialize variables
        water = 0
        cur_row = []
        # iterate through each element in the row
        for el in row:
            if el == 0:
                cur_row.append(0)
            elif el == 1:
                cur_row.append(1)
                water += 1
        if sum(cur_row) == 0:
            return 0
        # sum up all the 1s in the row
        # if you can extract this amount of water using 1 bucket, then the row can be emptied
        # if you can't extract all the water, then the row can't be emptied
        if water <= capacity:
            return 1
        return 0

    def get_water(grid):
        """
        How many times can you extract water from the grid

        Args:
            grid (list): list of lists
        Returns:
            int: number of times you can extract water from the grid
        """
        # initialize variables
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        # iterate through each row
        for i in range(rows):
            count += extract_water(grid[i])
        return count

    # initialize variables
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    # iterate through each row
    for i in range(rows):
        count += extract_water(grid[i])
    return count

