
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

    def dfs(y, x, capacity, visited, count):
        if y >= len(grid) or y < 0:
            return count
        if x >= len(grid[0]) or x < 0:
            return count
        if grid[y][x] == 0 or visited[y][x]:
            return count

        visited[y][x] = True
        count = count + 1
        if capacity - grid[y][x] < 0:
            return count

        if capacity - grid[y][x] == 0:
            return count

        return dfs(y + 1, x, capacity - grid[y][x], visited, count) + \
               dfs(y - 1, x, capacity - grid[y][x], visited, count) + \
               dfs(y, x + 1, capacity - grid[y][x], visited, count) + \
               dfs(y, x - 1, capacity - grid[y][x], visited, count)

    def print_grid(grid):
        for row in grid:
            print(row)
        print()

    # print_grid(grid)
    count = 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    capacity = 0
    for row in grid:
        for val in row:
            capacity = capacity + val
    if capacity <= 0:
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count = max(count, dfs(i, j, capacity, visited, 0))
    return count

