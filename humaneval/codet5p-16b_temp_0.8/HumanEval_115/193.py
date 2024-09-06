
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

    def get_wells_with_capacity(grid, capacity):
        wells = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    wells.append((row, col))
        return wells
    
    def get_water_needed(wells, capacity):
        water_needed = 0
        for row, col in wells:
            water_needed += capacity - grid[row][col]
        return water_needed

    def find_min_num_of_buckets(water_needed, capacity):
        if water_needed == 0: return 0
        if capacity == 1: return -1 # inf because of math.inf

        water_needed = math.ceil(water_needed / capacity)
        return water_needed + find_min_num_of_buckets(water_needed, capacity - 1)

    wells = get_wells_with_capacity(grid, capacity)
    water_needed = get_water_needed(wells, capacity)
    return find
