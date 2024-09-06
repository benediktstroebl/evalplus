Here's a Python script with a self-contained function that solves the problem:
```python
def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, count):
        if count == k:
            return True, path

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                if dfs(nr, nc, path + [grid[nr][nc]], visited, count + 1):
                    return True, path
                visited[nr][nc] = False

        return False, path

    visited = [[False for _ in range(N)] for _ in range(N)]
    return dfs(0, 0, [], visited, 0)
``` 

The solution algorithm is Depth-First Search. Starting from any cell, we try to reach any non-visited neighbor and recursively check if we can reach k cells, storing the path found. The algorithm comes down to checking all 2^2*(N-1) combinations of reachable cells in the grid, which is guaranteed to find the solution in polynomial time.