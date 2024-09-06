Here's a Python script with a self-contained function that solves the problem:
```python
def minPath(grid, k):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(k + 1)]
    for i in range(k + 1):
        dp[i][0] = 0
    for i in range(1, n):
        for j in range(1, k + 1):
            dp[j][i] = min(dp[j][i - 1], dp[j - 1][i])
            if grid[i - 1][j - 1] < dp[j][i]:
                dp[j][i] = grid[i - 1][j - 1]
    return dp[k][-1]
```

The overall idea is to use dynamic programming to build a minimum path of length `k` by iteratively selecting the minimum value in the reachable cells. At every step, you have two options: move to the cell with the minimum value among the reachable cells or stay in the current cell. The dp array is used to store the minimum path value that ends at each cell in the grid and ensures that the answer is unique.