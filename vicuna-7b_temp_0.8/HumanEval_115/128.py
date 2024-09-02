
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
    # Initialize the number of times buckets need to be lowered
    num_of_times = 0
    
    # Iterate through the rows of grid
    for i in range(grid.length):
        # Iterate through the columns of grid
        for j in range(grid[i].length):
            # Check if all the wells in the row are empty
            if not grid[i][j]:
                # If the row is empty, fill it with water
                grid[i][j] = True
                bucket_index = j * grid[i].length + i + 1
                bucket_index = min(bucket_index, grid.length - 1)
                for k in range(bucket_index, grid.length):
                    grid[k][j] = False
                num_of_times += 1
                
    # Return the number of times buckets need to be lowered
    return num_of_times
