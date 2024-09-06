
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
    n = len(grid)
    m = len(grid[0])
    # The amount of times you need to lower the buckets to empty the wells
    times = 0
    # Iterate over the grid and extract the water
    for i in range(n):
        j = 0
        while j < m:
            # If the well is already empty, go to next row
            if grid[i][j] == 0:
                break
            # If there is enough water to fill the bucket
            if grid[i][j] <= capacity:
                # Empty the bucket
                for k in range(i, n):
                    grid[k][j] = 0
                # Reset the bucket
                times += 1
                j += 1
                continue
            # Fill the bucket with the max amount of water
            bucket = 0
            for k in range(i, n):
                if (bucket + grid[k][j]) < capacity:
                    bucket += grid[k][j]
                else:
                    for l in range(k, n):
                        grid[l][j] -= bucket
                    times += math.ceil(bucket / capacity)
                    break
    return times
