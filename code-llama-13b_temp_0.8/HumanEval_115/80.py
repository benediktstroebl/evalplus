
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
    # Sum the total number of wells
    total_wells = sum([sum(row) for row in grid])
    # Calculate the total number of times the buckets need to be lowered
    # to empty all the wells
    total_buckets = math.ceil(total_wells/capacity)
    # To empty the wells, we will also need a top-down traversal of the grid
    # to "pour water" into all the wells
    # The wells are filled in a bottom-up fashion
    # for example, if the last bucket is 1, we don't need to pour
    # 1 bucket into the 1st row, we need to pour 1 bucket into the 1st well
    # of the 1st row, which is equivalent to filling the 1st row
    for bucket in reversed(range(total_buckets)):
        # Traverse the grid
        for i in range(len(grid)):
            # Traverse the row
            for j in range(len(grid[i])):
                # We only care about the wells that were filled in previous steps
                # We can ignore all the rest
                if grid[i][j] == 0:
                    continue
                # Check if the bucket is equal to or less than the well
                if bucket < grid[i][j]:
                    # If it's less than the well, pour all the water
                    grid[i][j] = bucket
                else:
                    # If it's equal to the well, we have no more water to pour
                    # into this well
                    grid[i][j] = 0
    # Calculate the total number of times the buckets have been lowered
    return total_buckets
