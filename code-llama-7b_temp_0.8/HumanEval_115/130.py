
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
    def dfs(grid, row, col, capacity, visited, buckets):
        # Base case: reached the end of the grid
        if row == len(grid) - 1:
            return buckets

        # Base case: reached the end of the row
        if col == len(grid[0]) - 1:
            return dfs(grid, row + 1, 0, capacity, visited, buckets)
        
        # Base case: reached a visited cell
        if visited[row][col]:
            return dfs(grid, row, col + 1, capacity, visited, buckets)

        # Recursive step: explore the next cell
        # If the next cell is water, fill it in the bucket and move on to the next cell
        if grid[row][col] == 1:
            buckets += 1
            visited[row][col] = True
            return dfs(grid, row, col + 1, capacity, visited, buckets)
        # If the next cell is empty, move on to the next cell
        elif grid[row][col] == 0:
            return dfs(grid, row, col + 1, capacity, visited, buckets)

    # Initialization
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]

    # Loop through each well
    # After filling up the buckets, move to the next well
    buckets = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            buckets = dfs(grid, i, j, capacity, visited, buckets)
    
    return buckets
