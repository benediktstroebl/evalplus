
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

    def dfs(grid, i, j, capacity, visited):
        if (i,j) in visited:
            return
        visited.add((i,j))
        if grid[i][j] == 1:
            dfs(grid, i, j-1, capacity, visited)
            dfs(grid, i, j+1, capacity, visited)
        if grid[i][j] == 0:
            dfs(grid, i-1, j, capacity, visited)
            dfs(grid, i+1, j, capacity, visited)
            dfs(grid, i, j-1, capacity, visited)
            dfs(grid, i, j+1, capacity, visited)
            return
        capacity -= 1
        for k in range(4):
            for n in range(grid.length):
                for o in range(grid[0].length):
                    if (k,n,o) not in visited:
                        dfs(grid, i+1, j-k, capacity, visited)
                        dfs(grid, i+1, j+k, capacity, visited)
                        dfs(grid, i-1, j+n, capacity, visited)
                        dfs(grid, i-1, j-n, capacity, visited)
                        dfs(grid, i+1, j-n-o, capacity, visited)
                        dfs(grid, i-1, j+n+o, capacity, visited)
                        return

    visited = set()
    grid = [int(x) for x in grid]
    for i in range(grid.length):
        for j in range(grid[0].length):
            if grid[i][j] == 1:
                dfs(grid, i, j, capacity, visited)
    return len(visited)