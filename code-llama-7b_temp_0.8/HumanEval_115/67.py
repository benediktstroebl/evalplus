
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
    def distribute_water(grid, capacity):
        """
        Time: O(n)
        Space: O(n)
        """
        from collections import deque

        # find wells
        wells = []
        for row in grid:
            for i, water_unit in enumerate(row):
                if water_unit:
                    wells.append(i)

        # find buckets
        n = len(grid[0])
        buckets = deque()
        for i in range(n):
            if grid[0][i]:
                buckets.append(i)

        # distribute
        water_count = 0
        while buckets:
            bucket_i = buckets.popleft()
            for well_i in wells:
                if well_i >= bucket_i:
                    if grid[well_i][bucket_i]:
                        water_count += 1
                        grid[well_i][bucket_i] = 0
                else:
                    if grid[well_i][bucket_i]:
                        buckets.append(bucket_i)
                        break

        return water_count
    
    def max_wells_filled(grid, bucket_capacity):
        """
        Time: O(n^2)
        Space: O(n^2)
        """
        n = len(grid)
        m = len(grid[0])
        water_matrix = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                water_matrix[i][j] = distribute_water(grid[i:i+bucket_capacity], m)

        return sum(min(water_matrix[i][j] for i in range(n)) for j in range(m))

    n = len(grid)
    m = len(grid[0])
    if n == 0 or m == 0:
        return 0
    if capacity >= n * m:
        return capacity * n

    return max_wells_filled(grid, capacity)
