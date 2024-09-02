
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
    def add_water(grid, bucket_capacity):
        """
        Returns a tuple with water level and number of times buckets were lowered
        """
        def calc_water(row):
            return row.count(1)

        def calc_buckets(row):
            return row.count(0)

        water_level = 0
        for row in grid:
            water_level += calc_water(row)

        buckets = 0
        for row in grid:
            buckets += calc_buckets(row)

        return water_level, buckets

    def lower_buckets(grid, bucket_capacity):
        """
        Returns number of times buckets were lowered
        """
        def calc_water(row):
            return row.count(1)

        def calc_buckets(row):
            return row.count(0)

        for row in grid:
            water_level = calc_water(row)
            buckets = calc_buckets(row)

            lowered = 0
            for i in range(len(row)):
                if row[i] == 0:
                    water_level -= 1
                    if water_level == 0:
                        row[i] = 1
                        buckets -= 1
                        lowered += 1
                    else:
                        row[i] = 1

        return lowered

    def convert_grid(grid, bucket_capacity):
        """
        Converts grid to a list of lists
        """
        return [list(row) for row in grid]

    def fill_wells(grid, bucket_capacity):
        """
        Returns the number of times buckets were lowered
        """
        # convert grid to list of lists
        converted_grid = convert_grid(grid, bucket_capacity)

        # add water to wells
        water_level, buckets = add_water(converted_grid, bucket_capacity)

        # lower buckets
        lowered = lower_buckets(converted_grid, bucket_capacity)

        return lowered

    
