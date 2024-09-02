
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

    if capacity < 1 or capacity > 10:
        raise ValueError("Capacity must be between 1 and 10")

    # Flood-fill the grid with capacity-1 to create a huge water tank.
    tank = []
    for i in range(len(grid)):
        tank.append([])
        for j in range(len(grid[i])):
            tank[i].append(capacity - 1)

    # Replace all the 1's in the grid with 0's
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                tank[i][j] = 0

    # Replace the water tank with 0's
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tank[i][j] = 0

    # Return the number of times you need to lower the buckets
    return sum(tank) // capacity
