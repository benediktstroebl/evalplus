
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

    def fill_well(well, well_capacity):
        if not well:
            return 0
        if not well[1]:
            return 0
        if len(well) == 1:
            return math.inf
        buckets = [0]*well_capacity
        for i, bucket in enumerate(buckets):
            bucket += well[0]
            well[0] -= 1
            buckets[i] = bucket
        return buckets
    def find_max(wells, capacity):
        if len(wells) == 1:
            return 0
        fill = [[None]*len(wells) for _ in range(capacity)]
        for well in wells:
            fill[0][wells.index(well)] = fill_well(well, capacity)
        for i in range(1, capacity):
            for j in range(len(wells)):
                fill[i][j] = max([fill[i-1][k]+fill_well(wells[j], capacity-i) for k, well in enumerate(wells)])
        return fill[capacity-
