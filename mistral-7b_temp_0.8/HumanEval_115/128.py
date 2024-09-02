
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
    def is_valid(r, c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
    def dfs(r, c, visited, capacity):
        if not is_valid(r, c):
            return 0
        if (r, c) in visited:
            return 0

        visited.add((r, c))
        if grid[r][c] == 0:
            return 1
        res = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            res += dfs(r + dr, c + dc, visited, capacity)
        return res

    visited = set()
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                res += dfs(r, c, visited, capacity)
    return res

    # Time complexity : O(
