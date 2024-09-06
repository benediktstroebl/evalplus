
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
    if len(grid) == 0:
        return 0
    def get_water(grid):
        n = len(grid[0])
        water = [0 for _ in range(n)]
        for row in grid:
            for i in range(n):
                if row[i] == 1:
                    water[i] += 1
        return water
    
    def get_bucket_count(grid):
        n = len(grid[0])
        count = 0
        for row in grid:
            if any(row):
                count += 1
        return count

    def get_buckets(grid, bucket_capacity):
        n = len(grid[0])
        water = [0 for _ in range(n)]
        for row in grid:
            for i in range(n):
                if row[i] == 1:
                    water[i] += 1
        count = get_bucket_count(grid)
        b = []
        for i in range(n):
            b.append(min(water[i], bucket_capacity))
        return b, count
    
    def lower_buckets(grid, bucket_capacity, buckets):
        import math
        count = 0
        n = len(grid[0])
        while True:
            empty_wells = 0
            for i in range(n):
                if grid[0][i] == 1:
                    grid[0][i] = 0
                    empty_wells += 1
            if empty_wells == 0:
                break
            for i in range(1, len(grid)):
                for j in range(n):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
            count += 1
        return count
    
    if capacity == 0:
        return 0
    
    water = get_water(grid)
    buckets, bucket_count = get_buckets(grid, capacity)
    if bucket_count == 0:
        return 0
    count = 0
    while True:
        count += 
