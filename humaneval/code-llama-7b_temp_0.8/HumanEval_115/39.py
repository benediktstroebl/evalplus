
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
    import math
    def bucket_fill(grid, capacity):
        """
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        capacity = 1
        return 6
        """
        import math
        i = 0
        while i < len(grid):
            # find first row with water
            while not any(grid[i]):
                i += 1
                if i >= len(grid):
                    return 0
            # find first bucket with capacity
            j = 0
            while grid[i][j] <= capacity:
                j += 1
            # move water from first row to first bucket
            for j in range(len(grid[0])):
                if grid[i][j]:
                    grid[0][j] -= 1
                    grid[j][0] += 1
            # find first filled bucket
            j = 0
            while not grid[0][j]:
                j += 1
            # move water from first bucket to first filled bucket
            for i in range(1, len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] and grid[j][0]:
                        grid[i][j] -= 1
                        grid[j][0] += 1
            i = 0
        return len(grid) - 1

    def drain_buckets(grid, capacity):
        """
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        capacity = 2
        return 5
        """
        import math
        for i in range(len(grid)):
            while any(grid[i]):
                for j in range(len(grid[i])):
                    if grid[i][j]:
                        grid[i][j] -= 1
                        grid[i][j % len(grid[i])] += 1
        return len(grid) - 1

    def max_fill_buckets(grid, capacity):
