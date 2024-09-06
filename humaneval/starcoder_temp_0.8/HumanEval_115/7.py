
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
    if not grid or not grid[0]:
        return 0

    def fill_well(grid, x, y, capacity):
        if not grid[x][y]:
            return 0
        
        # If we can fill the well, first fill it completely, then get the number of
        # times we need to lower the buckets to empty the well
        # 
        # Then, check if we can fill any of the well's neighbours. We do this in 2 passes:
        #     * first we fill a well if the bucket is empty
        #     * then we fill all neighbouring wells if the bucket is not empty
        # 
        # Note: we only do this if the bucket has capacity > 0

        # fill well
        fill_count = 0
        bucket_used = capacity
        while bucket_used < grid[x][y] and fill_count < grid[x][y]:
            bucket_used += capacity
            fill_count += 1

        # fill neighbours
        if x > 0 and grid[x-1][y] and grid[x-1][y] < capacity:
            grid[x-1][y] -= capacity
            fill_well(grid, x-1, y, capacity)
        if x < len(grid) - 1 and grid[x+1][y] and grid[x+1][y] < capacity:
            grid[x+1][y] -= capacity
            fill_well(grid, x+1, y, capacity)
        if y > 0 and grid[x][y-1] and grid[x][y-1] < capacity:
            grid[x][y-1] -= capacity
            fill_well(grid, x, y-1, capacity)
        if y < len(grid[0]) - 1 and grid[x][y+1] and grid[x][y+1] < capacity:
            grid[x][y+1] -= capacity
            fill_well(grid, x, y+1, capacity)

        return fill_count

    fill_count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            fill_count += fill_well(grid, x, y, capacity)
    return fill_count
