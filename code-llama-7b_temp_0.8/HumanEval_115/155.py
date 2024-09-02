
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

    def get_no_of_times(grid, capacity):
        no_of_times = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if capacity == 0:
                        no_of_times += 1
                    else:
                        capacity -= 1
                    grid[i][j] = 0

        return no_of_times, grid

    def get_min_max_range(grid, capacity):
        max_range = 0
        min_range = math.inf
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_range = max(max_range, i)
                    min_range = min(min_range, i)

        return max_range, min_range, grid

    def get_max_capacity(grid):
        max_capacity = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_capacity += 1
        return max_capacity

    def get_no_of_times_optimized(grid, capacity):
        no_of_times = 0
        max_capacity = get_max_capacity(grid)
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if capacity == 0:
                        no_of_times += 1
                    else:
                        capacity -= 1
                    grid[i][j] = 0

        return no_of_times, grid, max_capacity

    def get_no_
