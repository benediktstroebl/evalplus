
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

    def fill_well(well, capacity):
        if len(well) == 1:
            return 0
        water = math.floor(capacity / len(well))
        water = water if water >= 1 else 1
        return water
    
    def drain_well(well, capacity, water):
        if capacity >= water:
            capacity -= water
            return capacity
        elif water > capacity:
            water -= capacity
            capacity = 0
            return capacity
        else:
            capacity = 0
            return capacity
        
    rows = len(grid)
    cols = len(grid[0])
    water = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                bucket_capacity = capacity
                well = [row, col]
                water += 1
                while bucket_capacity > 0:
                    water += fill_well(well, bucket_capacity)
                    bucket_capacity = drain_well(well, bucket_capacity, water)
    return water


