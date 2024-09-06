
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

    n, m = len(grid), len(grid[0])

    def get_well_with_max_water(grid, bucket_capacity):
        max_water = 0
        for i in range(n):
            for j in range(m):
                water = bucket_capacity * grid[i][j]
                if water > max_water:
                    max_water = water
        return max_water

    def get_well_with_min_water(grid, bucket_capacity):
        max_water = math.inf
        for i in range(n):
            for j in range(m):
                water = bucket_capacity * grid[i][j]
                if water < max_water:
                    max_water = water
        return max_water

    if grid[0][0]!= 1:
        raise ValueError("Grid should start with a well")
    
    well_with_max_water = get_well_with_max_water(grid, capacity)
    well_with_min_water = get_well_with_min_water(grid, capacity)
    return well
