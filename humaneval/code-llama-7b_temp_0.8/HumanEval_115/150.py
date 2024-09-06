
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

    def find_max_well_length(grid):
        """
        Find the longest row in a grid.
        """
        longest_well_length = 0
        for row in grid:
            if len(row) > longest_well_length:
                longest_well_length = len(row)

        return longest_well_length

    def find_well_count(grid):
        """
        Find the total number of wells.
        """
        return len(grid)

    def find_empty_wells(grid):
        """
        Find the number of empty wells.
        """
        empty_wells = 0
        for row in grid:
            if row.count(0) == len(row):
                empty_wells += 1
        
        return empty_wells

    def find_bucket_count(grid, well_count):
        """
        Find the number of buckets needed to empty all wells.
        """
        return math.ceil(well_count / len(grid))

    def find_max_well_capacity(grid):
        """
        Find the maximum number of units of water that can be placed in a single well.
        """
        well_capacity = 0
        for row in grid:
            if row.count(1) > well_capacity:
                well_capacity = row.count(1)

        return well_capacity

    def find_bucket_count_for_wells(bucket_count, well_count, well_capacity):
        """
        Find the maximum number of buckets needed to empty all wells.
        """
        buckets_for_wells = 0
        remaining_wells = well_count
        while remaining_wells > 0:
            buckets_for_wells += well_capacity
            remaining_wells -= well_capacity

        return buckets_for_wells

    def find_max_buckets(grid, bucket_capacity, well_count):
        """
        Find the maximum number of buckets needed to empty all wells.
        """
        buckets = 0
        remaining_water
