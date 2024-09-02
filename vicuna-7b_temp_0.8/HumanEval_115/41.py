
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
    # Create an empty list to store the number of times we need to lower the buckets
    num_of_times = [0] * grid.shape[0]
    # Loop through all the wells
    for i in range(grid.shape[0]):
        # Loop through all the buckets
        for j in range(grid.shape[1]):
            # Check if the well is full
            if grid[i][j] == 1:
                # If it's full, we need to lower the bucket
                num_of_times[i] += 1
                grid[i][j] = 0
    # Find the maximum number of times we need to lower the buckets
    max_num_of_times = max(num_of_times)
    return max_num_of_times
