
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

    # PSEUDOCODE
    # 1. Check if we are able to fit the water in the wells
    # 2. Calculate the max water per well from the bottom and from the top
    # 3. If the capacity is not enough, we can fill it as much as possible

    # Find the length of the wells
    n = len(grid)
    # Define the output variable to hold the count
    count = 0
    # Loop through the wells
    for i in range(n):
        # Check if the first column has water
        if grid[i][0] == 1:
            # Check if the capacity is enough to fill it
            if capacity >= n:
                # If yes, increment the count
                count += n
            else:
                # If no, increment the count and assign the capacity as the water amount to be filled
                count += capacity
        # Calculate the max water in the well from the bottom
        max_bottom = n - i
        # Calculate the max water in the well from the top
        max_top = i + 1
        # Find the max water
        max_water = min(max_bottom, max_top)
        # If the capacity is not enough to fill it
        if capacity < max_water:
            # Fill it as much as possible
            count += capacity
        else:
            # Fill it with the max water
            count += max_water
            # Adjust the capacity
            capacity -= max_water
    
    return count
