
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
    # Brute Force:
    # Iterate over all cells
    # If a cell is not visited
    #   Get the maximum number of fills from all possible permutations
    #   Use a cache to avoid repeated computation of this number for the same cell
    # Return the maximum value
    #
    # Complexity Analysis
    # Time Complexity: O(n!)
    # Space Complexity: O(n!)

    def fill(grid, i, j):
        if i == -1 or j == -1:
            return 0
        if grid[i][j] == 1:
            return 0
        if cache[(i, j)]!= -1:
            return cache[(i, j)]
        if grid[i][j] == 0:
            cache[(i, j)] = math.inf
            for m in range(i, len(grid)):
                cache[(i, j)] = min(fill(grid, m, j) + 1, cache[(i, j)])
            for n in range(j, len(grid[0])):
                cache[(i, j)] = min(fill(grid, i, n) + 1, cache[(i, j)])
        return cache[(i, j)]

    cache = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cache[(i, j)] = -1
    return fill(grid, 0, 0)

