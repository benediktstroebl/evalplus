
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

    max_depth = 0
    buckets = 0
    visited = set()

    def depth_first_search(grid, row, col):
        if (row, col) in visited:
            return

        if grid[row][col] == 0:
            return

        if max_depth < grid[row][col]:
            max_depth = grid[row][col]

        visited.add((row, col))

        for x, y in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                depth_first_search(grid, x, y)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                continue

            if (row, col) in visited:
                continue

            depth_first_search(grid, row
