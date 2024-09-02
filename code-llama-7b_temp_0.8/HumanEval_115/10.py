
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
    #Method 1
    # def max_fill(grid, bucket_capacity):
    #     rows, cols = len(grid), len(grid[0])
    #     max_water = 0
    #     for row in range(rows):
    #         for col in range(cols):
    #             max_water += (min(grid[row][col], grid[row][cols - 1 - col]) * (col - row))
    #     return math.ceil(max_water / bucket_capacity)

    #Method 2
    def max_fill(grid, bucket_capacity):
        # Columns
        for col in range(len(grid[0])):
            max_water = 0
            for row in range(len(grid)):
                max_water += grid[row][col]
            for row in range(1, len(grid)):
                if grid[row][col] != 0:
                    max_water -= grid[row][col]
                else:
                    break
            for row in range(len(grid) - 1, 0, -1):
                if grid[row][col] != 0:
                    max_water -= grid[row][col]
                else:
                    break
            grid[0][col] += max_water

        # Rows
        for row in range(len(grid)):
            max_water = 0
            for col in range(len(grid[0])):
                max_water += grid[row][col]
            for col in range(1, len(grid[0])):
                if grid[row][col] != 0:
                    max_water -= grid[row][col]
                else:
                    break
            for col in range(len(grid[0]) - 1, 0, -1):
                if grid[row][col] != 0:
                    max_water -= grid[row][col]
                else:
                    break
            grid[row][0] += max_water

        return math.ceil(max(grid[row][col] for row in range(len(grid)) for col in range(len(grid[0
