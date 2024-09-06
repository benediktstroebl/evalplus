
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
    """
    This is a graph problem
    The graph is well-defined by its edges
    The graph is acyclic
    DFS to find
    """
    ## avoid edge case
    if not grid or capacity == 0:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    color = {}
    zipped_grid = [[] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            zipped_grid[i].append(grid[i][j])
            if grid[i][j]:
                color[(i, j)] = 'W'
            else:
                color[(i, j)] = 'P'

    def dfs(x, y, c, zipped_grid, color, capacity, count):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return
        if color[(x, y)] == 'W':
            return
        else:
            if color[(x, y)] == 'P':
                if zipped_grid[x][y] <= capacity:
                    count[0] += 1
                return
            else:
                dfs(x - 1, y, c, zipped_grid, color, capacity, count)
                dfs(x + 1, y, c, zipped_grid, color, capacity, count)
                dfs(x, y - 1, c, zipped_grid, color, capacity, count)
                dfs(x, y + 1, c, zipped_grid, color, capacity, count)

    def process_color(color, visited):
        rows = len(color)
        cols = len(color[0])
        for i in range(rows):
            for j in range(cols):
                if color[(i,j)] == 'P' and (i,j) not in visited:
                    visited.add((i,j))
                    dfs(i, j, 0, zipped_grid, color, capacity, [0])

    visited = set()
    process_color(color, visited)
    return count[0]

