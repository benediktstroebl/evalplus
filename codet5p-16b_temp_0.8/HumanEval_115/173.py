
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

    num_wells = len(grid)
    num_buckets = len(grid[0])

    def get_score(r, c):
        return math.floor((num_wells - r - 1) * (num_buckets - c - 1))

    def dfs(grid, r, c, bucket_capacity):
        if r >= num_wells or c >= num_buckets:
            return 0
        if grid[r][c] == 0:
            return 0
        max_fill = min(bucket_capacity, grid[r][c])
        grid[r][c] -= max_fill
        score = max_fill * (max_fill + 1) // 2
        return max(score, dfs(grid, r + 1, c, bucket_capacity), dfs(grid, r, c + 1, bucket_capacity), dfs(grid, r + 1, c + 1, bucket_capacity)) + 1
    return dfs(grid, 0, 0, capacity)

