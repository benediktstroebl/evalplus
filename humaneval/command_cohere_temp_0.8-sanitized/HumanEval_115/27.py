import math
def max_fill(grid, capacity):
    grid = [list(row) for row in grid]
    n = len(grid)
    m = len(grid[0])
    visited = [False] * (m)
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[j] and grid[i][j] == 1:
                count += 1
                visited[j] = True
                count += max_fill(grid, capacity, i, j) // capacity
    return count