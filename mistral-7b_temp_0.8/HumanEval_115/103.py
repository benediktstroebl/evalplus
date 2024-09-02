
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
    
    # Solution
    
    def dfs(grid, capacity, height, rows, cols, steps):
        """
        Recursive function that fills each well and returns the number of steps taken.
        """
        # Base case
        if not rows or not cols:
            return 0
        # Otherwise
        new_steps = steps + grid[height][0]
        if grid[height][0] >= capacity:
            return new_steps
        # Fill the well
        grid[height][0] -= capacity
        # Go down
        new_steps = dfs(grid, capacity, height+1, rows-1, cols, new_steps)
        # Go right
        new_steps = dfs(grid, capacity, height, rows, cols-1, new_steps)
        # Go left
        new_steps = dfs(grid, capacity, height, rows, cols-1, new_steps)
        # Go up
        new_steps = dfs(grid, capacity, height-1, rows-1, cols, new_steps)
        # Return the
