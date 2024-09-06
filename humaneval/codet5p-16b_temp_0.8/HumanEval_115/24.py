
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

    def get_next_well(grid, capacity):
        nonlocal wells
        wells = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    wells.append((i,j))
                    return (i,j)
        return None

    def get_next_bucket(well, bucket_capacity):
        nonlocal buckets, grid
        for i in range(len(grid)):
            if grid[i][well[1]]!= 0:
                buckets.append((i,well[1], bucket_capacity))
                grid[i][well[1]] -= bucket_capacity
                return (i,well[1], bucket_capacity)
        return None

    def empty_well(well, bucket_capacity):
        nonlocal buckets
        while (len(buckets) > 0) and (buckets[0][2] == bucket_capacity):
            grid[buckets[0][0]][buckets[0][1]] += buckets[0][2]
            buckets
