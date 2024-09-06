
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
    rows = len(grid)
    cols = len(grid[0])
    grid = [[1 if i==1 else 0 for i in row] for row in grid]
    
    def is_well_empty(well):
        """
        Returns whether a well is empty.
        """
        for col in range(cols):
            if well[col] == 1:
                return False
        return True
    
    def fill_well(well, fill_val):
        """
        Fills a well with a value, if it's not full.
        """
        for col in range(cols):
            if well[col] == 0:
                well[col] = fill_val
    
    def fill_wells(wells):
        """
        Tries to fill all wells with 1.
        """
        well_filled = False
        for col in range(cols):
            for well in wells:
                if well[col] == 0:
                    fill_well(well, 1)
                    well_filled = True
        return well_filled
    
    def empty_wells(wells):
        """
        Empties all wells with 0.
        """
        for well in wells:
            fill_well(well, 0)
    
    def fill_buckets(buckets, wells):
        """
        Fills a given number of buckets with water.
        """
        for bucket in range(buckets):
            for well in wells:
                fill_well(well, 1)
    
    def is_bucket_full(buckets):
        """
        Returns whether a bucket is full.
        """
        for well in buckets:
            for col in range(cols):
                if well[col] == 0:
                    return False
        return True
    
    def is_wells_filled(wells):
        """
        Returns whether all wells are filled.
        """
        for well in wells:
            if is_well_empty(well):
                return False
        return True
    
    def count_fills(buckets, wells):
