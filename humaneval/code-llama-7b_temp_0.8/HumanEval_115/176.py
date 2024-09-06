
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
    # TODO: finish the docstring
    def is_empty(row):
        if row[0] == 0:
            return True
        else:
            return False

    def is_full(row):
        if row.count(1) == capacity:
            return True
        else:
            return False

    def find_empty_well(grid):
        for row in grid:
            if is_empty(row):
                return grid.index(row)

    def find_full_well(grid):
        for row in grid:
            if is_full(row):
                return grid.index(row)

    def find_empty_bucket(grid, cap):
        for row in grid:
            if row.count(1) < cap:
                return grid.index(row)

    def find_full_bucket(grid, cap):
        for row in grid:
            if row.count(1) == cap:
                return grid.index(row)

    def transfer_water(grid, buckets, capacity):
        rows = len(grid)
        cols = len(grid[0])
        iters = 0
        empty_well = find_empty_well(grid)
        # Check if empty well exists, else return 0
        if empty_well is None:
            return iters
        else:
            while empty_well is not None:
                iters += 1
                if grid[empty_well].count(1) < capacity:
                    # get remaining
                    empty_water = capacity - grid[empty_well].count(1)
                    full_bucket = find_full_bucket(buckets, empty_water)
                    # Check if full bucket exists, else return -1
                    if full_bucket is None:
                        return -1
                    else:
                        # find number of empty spots
                        row_bucket = buckets[full_bucket]
                        num_empty = row_bucket.count(0)
                        # find how many can fit
                        fits = empty_water if empty_water < num_empty else num_empty
                        # how many are left over
                        left_
