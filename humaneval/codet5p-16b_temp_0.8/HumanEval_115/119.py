
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

    r = len(grid)
    c = len(grid[0])
    assert r >= 1
    assert c >= 1
    assert r == len(grid[0])
    assert capacity >= 1
    
    def get_wells(grid):
        wells = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    wells.append([i, j])
        return wells

    def get_buckets(grid, capacity):
        buckets = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    buckets.append([i, j, capacity])
        return buckets

    def get_units(grid):
        units = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    units.append([i, j])
        return units

    def get_distances(units, wells, buckets, capacity):
        dists = []
        
