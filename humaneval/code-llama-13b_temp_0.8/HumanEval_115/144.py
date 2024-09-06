
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
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Compute number of rows and columns
    rows, cols = len(grid), len(grid[0])
    # Get minimum number of times the buckets need to be lowered
    mins = 0
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Loop through the grid from left to right
    for c in range(cols):
        # Initialize the bucket capacity and the water level
        capacity, water = capacity, 0
        # Loop through the grid from top to bottom
        for r in range(rows-1, -1, -1):
            # If the current well has water
            if grid[r][c]:
                # Check if the bucket capacity can hold the water in the well
                if capacity - grid[r][c] >= 0:
                    capacity -= grid[r][c]
                # Otherwise, the bucket capacity is refilled and the water level is updated
                else:
                    water += capacity
                    capacity = grid[r][c] - capacity
            # Otherwise, no water is added
            else:
                water += capacity
            # Check if the water level is greater than or equal to the bucket capacity
            if water >= capacity:
                mins += math.ceil(water/capacity)
                water = 0
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    return mins
