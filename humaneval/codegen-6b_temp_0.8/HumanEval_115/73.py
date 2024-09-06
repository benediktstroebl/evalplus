
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
    m, n = len(grid), len(grid[0])

    well_values, grid = [], []
    for i in range(m):
        well_values.append(sum(grid[i]))
        grid.append([int(math.ceil(well_values[i] / capacity)) for _ in range(n)])

    # perform dfs and count the number of lower operations
    def dfs(row, col, grid, visited):
        if row < 0 or row >= m or col < 0 or col >= n:
            return 0
        if visited[row][col] == 1:
            return grid[row][col]
        visited[row][col] = 1
        return max(grid[row][col], dfs(row-1, col, grid, visited) + dfs(row, col-1, grid, visited), dfs(row+1, col, grid, visited) + dfs(row, col+1, grid, visited))

    visited = [[0 for _ in range(n)] for _ in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0 and visited[i][j] == 0:
                count += dfs(i, j, grid, visited)
    return count
