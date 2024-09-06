
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

    def dfs(row, col):
        # Avoid out of bounds or visited cells.
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
            return

        # Remove current cell.
        grid[row][col] = 0
        visited.add((row, col))
        num_filled += 1

        # Call recursively with adjacent cells.
        dfs(row, col - 1)
        dfs(row, col + 1)
        dfs(row - 1, col)
        dfs(row + 1, col)

    num_filled = 0
    visited = set()
    num_buckets = 0

    # Go through every well.
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the well is not empty call dfs to fill it.
            if grid[row][col] == 1:
                dfs(row, col)
                num_buckets += 1
    
    # We can empty all wells in the same number of buckets.
    return int(math.ceil(num_filled / capacity)) if num_filled > 0 else 0
