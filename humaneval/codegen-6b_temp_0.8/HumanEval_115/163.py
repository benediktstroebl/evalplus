
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
    # O(n^2 * m) time
    # O(n) space
    import math
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        left = dfs(r, c - 1)
        right = dfs(r, c + 1)
        up = dfs(r - 1, c)
        down = dfs(r + 1, c)
        return 1 + max(left, right, up, down)

    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    max_well = max(map(max, grid))
    max_well_x = max_well + capacity

    # how many buckets we need
    buckets_to_empty = math.ceil(n / max_well_x)
    return buckets_to_empty - dfs(m - 1, 0)
