def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Initialize the dp[][] with Value k+1 Everywhere
    dp = [[k + 1] * N for _ in range(N)]
    
    # Iterate through Every Cell
    for i in range(N):
        for j in range(N):
            # Ignore Cells with Value k+1
            if grid[i][j] == k + 1:
                continue
            
            # Update Adjacent Cells that are Smaller than Current Cell
            for nei in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= nei[0] < N and 0 <= nei[1] < N:
                    if grid[nei[0]][nei[1]] < grid[i][j]:
                        dp[nei[0]][nei[1]] = grid[i][j]
    
    # Track the Path
    path = []
    i, j = 0, 0
    while k > 0:
        for nei in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= nei[0] < N and 0 <= nei[1] < N and dp[nei[0]][nei[1]] == k:
                i, j = nei
                break
        path.append(grid[i][j])
        k -= 1
    
    return list(reversed(path))