
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
    # END OF PROBLEM STATEMENT

    # Initialize the visited array
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Initialize the maximum amount of water
    max_water = 0

    # Run through the grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            # Check if it's visited
            if not visited[row][column]:
                # Mark the current position as visited
                visited[row][column] = True
                # Get the maximum amount of water
                water = get_max(grid, row, column, capacity, visited)
                # If the water is greater than the current maximum, set it
                if water > max_water:
                    max_water = water
    return max_water

