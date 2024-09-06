
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
    
    # Time Complexity: O(n*m)
    # Space Complexity: O(n*m)
    def dfs(grid, i, j, capacity):
        if capacity < 0:
            return math.inf
        if i >= len(grid) or j >= len(grid[0]):
            return capacity
        if grid[i][j] == 0:
            return math.inf

        grid[i][j] = 0

        return min(capacity, dfs(grid, i, j+1, capacity-1), dfs(grid, i+1, j, capacity-1))

    max_buckets = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_buckets = max(max_buckets, dfs(grid, i, j, capacity))
    
    return max_buckets

