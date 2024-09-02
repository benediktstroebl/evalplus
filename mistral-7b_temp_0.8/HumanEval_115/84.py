
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
    # Naive solution
    # Use a simple dp
    # For each cell in the grid, add a column to represent the number of times
    # each cell is visited
    # For each cell in the grid, update the visited cell to the max of the visited cell
    # and the previous cell + capacity

    # Edge cases:
    # If the grid is empty, return 0
    # If the grid is only 1s, return the number of cells
    # If the capacity is 0, return the number of cells
    # If the capacity is larger than the number of cells, return 0

    # Time complexity: O(N^2)
    # Space complexity: O(N^2)
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    n = len(grid)
    m = len(grid[0])

    # Use a simple dp
    # For each cell in the grid, add a column to represent the number of times
    # each cell is visited
    # For each cell
