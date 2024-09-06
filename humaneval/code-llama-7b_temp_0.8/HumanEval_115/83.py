
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

    buckets = []
    wells = []

    def find_all_wells():
        for i in range(len(grid)):
            well = []
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    well.append((i, j))
            wells.append(well)

    def add_bucket():
        buckets.append(0)

    def remove_bucket(bucket_index):
        bucket_water = buckets[bucket_index]
        buckets.pop(bucket_index)
        return bucket_water

    def check_bucket_water(bucket_index):
        if buckets[bucket_index] == 0:
            return False
        else:
            return True

    def fill_buckets():
        for i in range(len(buckets)):
            bucket_water = remove_bucket(i)
            if bucket_water > 0:
                well = wells[i]
                if len(well) > 0:
                    fill_water = bucket_water if bucket_water < len(well) else len(well)
                    for j in range(fill_water):
                        well[j] = (well[j][0] - 1, well[j][1])
                    add_bucket()
                else:
                    buckets[i] = 0

    def lower_buckets():
        lower = 0
        for i in range(len(buckets)):
            if buckets[i] > 0:
                lower += 1
        return lower

    def fill_wells():
        for well in wells:
            add_bucket()
            if len(well) > 0:
                for well_location in well:
                    buckets[len(buckets) - 1] += 1
            else:
                buckets[len(buckets) - 1] = 0

    def fill_until_capacity():
        while capacity < len(grid):
            for i in range(len(wells)):
                if len(wells[i]) > 0:
                    capacity
