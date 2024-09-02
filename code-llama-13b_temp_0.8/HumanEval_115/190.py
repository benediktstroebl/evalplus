
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
    
    wells = len(grid)
    width = len(grid[0])
    total_water = 0

    # Sum the total amount of water in the grid
    for i in range(0, wells):
        for j in range(0, width):
            if grid[i][j] == 1:
                total_water += 1

    # Calculate the maximum amount of times the bucket can be lowered
    bucket_lower = math.ceil(total_water / capacity)

    # Initialize a 2d array
    grid_visited = [[False for i in range(0, width)] for j in range(0, wells)]

    # For each row in the grid
    for i in range(0, wells):
        # For each bucket capacity amount
        for x in range(0, bucket_lower):
            # For each column in the row
            for j in range(0, width):
                # If the cell is visited, skip it
                if grid_visited[i][j] == True:
                    continue
                # If the grid value is 1 and the capacity can still be filled
                if grid[i][j] == 1 and capacity > 0:
                    # Mark the cell as visited
                    grid_visited[i][j] = True
                    # Add the capacity to the current cell and reduce the capacity amount
                    grid[i][j] += capacity
                    capacity -= 1

    return total_water - (capacity * bucket_lower)
