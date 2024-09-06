def minPath(grid, k):
    n = len(grid)
    dp = [None] * (n * n)
    def dfs(r, c, prev):
        if k == 0:
            return grid[r][c]
        if dp[r * n + c] != None:
            return dp[r * n + c]
        maxi = float('-inf')
        mini = float('inf')
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if grid[nr][nc] > maxi:
                maxi = grid[nr][nc]
                neig = (nr, nc)
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if grid[nr][nc] < mini:
                mini = grid[nr][nc]
                neig = (nr, nc)
        if mini == float('inf'):
            return maxi
        if prev != -1:
            dp[r * n + c] = maxi if maxi == mini else mini
            return maxi if maxi == mini else mini
        ans = dfs(nr, nc, r * n + c)
        dp[r * n + c] = maxi if maxi == mini else mini
        return ans
    return dfs(0, 0, -1)