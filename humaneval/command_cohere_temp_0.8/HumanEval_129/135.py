```python
def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    for i in range(n):
        for j in range(n):
            dp[0][i] = grid[i][j]
    for length in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                dp[length][i] = min(dp[length][i], dp[length - 1][i])
                for nei in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= nei[0] < n and 0 <= nei[1] < n:
                        dp[length][i] = min(dp[length][i], dp[length - 1][nei[0]] + grid[nei[0]][nei[1]])
    return dp[k][0]
``` 

The DP table `dp` is filled as follows:
- `dp[0][i]` is the minimal path containing the cell `grid[i][j]` and of length 0.
- For `length > 0`, the value `dp[length][i]` is the minimal path containing the cell `grid[i][j]` and of length `length`, it considers the previous values of `dp[length - 1][i]` and the values in the grid cell neighbors.
- The output is `dp[k][0]`, which is the minimal path containing the top-left cell and of length `k`.

The script solves the problem efficiently in O((N^2)k).