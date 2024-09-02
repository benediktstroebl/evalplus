
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
    rows = grid.shape[0]
    cols = grid.shape[1]
    for i in range(rows):
        water_left = grid[i][:,1].tolist()
        water_left = [int(x) for x in water_left]
        for j in range(cols):
            if water_left[j] == 1:
                bucket_index = int(grid[i][j]) - 1
                bucket_capacity = int(bucket_capacity)
                num_of_buckets = math.ceil(max(0, (bucket_capacity - water_left[j]) / grid[i][j]) + 1)
                for k in range(num_of_buckets):
                    water_left[j] = 0
                water_left[j] += grid[i][j]
                if water_left[j] > bucket_capacity:
                    return num_of_buckets
    return 0