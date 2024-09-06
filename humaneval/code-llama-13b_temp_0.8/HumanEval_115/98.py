
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
    def fill_wells(grid, capacity):
        # fill the first row
        buckets = grid[0]
        water_spilled = 0
        for i in range(1, len(buckets)):
            if buckets[i] == 1:
                if buckets[i-1] == 0:
                    buckets[i] = 0
                else:
                    buckets[i-1] -= 1
            if buckets[i] == 0:
                water_spilled += 1
        # fill the other rows
        for i in range(1, len(grid)):
            buckets = grid[i]
            for j in range(len(buckets)):
                if buckets[j] == 0:
                    continue
                if buckets[j-1] == 0:
                    buckets[j-1] = 1
                    buckets[j] = 0
                elif buckets[j-1] >= capacity:
                    buckets[j-1] -= capacity
                    buckets[j] = 0
                else:
                    buckets[j-1] = 0
                    water_spilled += 1
        return water_spilled

    spilled = fill_wells(grid, capacity)
    total_wells = sum([sum(x) for x in grid])
    return math.floor(total_wells / capacity) + spilled

