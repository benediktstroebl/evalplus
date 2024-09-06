```python
def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    starts = set(range(n * n))
    for i in range(k + 1):
        for j in range(n):
            for ny in range(n):
                if (i, j, ny) not in starts:
                    continue
                starts.remove((i, j, ny))
                dp[i][j] = grid[j][ny]
                for nz in range(n):
                    if (i, j, nz) not in starts:
                        continue
                    starts.remove((i, j, nz))
                    dp[i][j] = min(dp[i][j], grid[j][ny] + dp[i - 1][nz])
    return dp[k][0]
``` 

The script uses a dynamic programming approach to construct the shortest path of length `k` on a grid. To keep track of the shortest path ending in each cell, it uses a `dp` matrix whose dimensions are `(k + 1) x n`, where `n` is the number of rows/columns in the grid. It also employs a `set` called `starts` to keep track of the cells from which the path can start. The function then iterates through each cell in the grid and fills in the `dp` matrix by considering all possible subsequent moves. The output is the k-length list of values that is the shortest path.