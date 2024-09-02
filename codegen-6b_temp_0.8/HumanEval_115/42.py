
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
    rows, cols = len(grid), len(grid[0])
    miss_water = [[0] * cols for _ in range(rows)]

    # for each well in the grid, determine the missing water
    for x in range(rows):
        for y in range(cols):
            if grid[x][y]:
                for xx in [x-1, x, x+1]:
                    for yy in [y-1, y, y+1]:
                        if xx >= 0 and xx < rows and yy >= 0 and yy < cols and not grid[xx][yy]:
                            miss_water[x][y] += 1

    # return count of missed wells
    return sum(sum(i) for i in miss_water) // capacity

