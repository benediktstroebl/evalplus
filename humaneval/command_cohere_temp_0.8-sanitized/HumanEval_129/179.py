def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1) for _ in range(k + 1)]
    seen = set()
    
    # Initialize the first column as the smallest cells
    for i in range(k + 1):
        dp[i][0] = 0
        start[i] = (0, 0)
    
    for i in range(1, N):
        for j in range(1, k + 1):
            min_j, min_idx = float('inf'), -1
            for di in range(N):
                for dj in range(N):
                    if (i, j) == (di, dj):
                        continue
                    if dp[j][di] != float('inf') and grid[i][dj] < grid[di][dj]:
                        if dp[j][di] + 1 < min_j:
                            min_j, min_idx = dp[j][di] + 1, (di, dj)
            dp[j][i] = min_j
            if min_j != float('inf') and (i, j) not in seen:
                seen.add((i, j))
                start[min_j] = (min_idx[0], min_idx[1])
    
    res = []
    while k > 0:
        x, y = start[k]
        res.append(grid[x][y])
        k -= 1
    return res[::-1]