def minPath(grid, k):
    N = len(grid)
    dp = [[float('inf')] * N for _ in range(k + 1)]
    start = [(-1, -1) for _ in range(k + 1)]

    def minPathHelper(currRow, currCol, length):
        if length == 0:
            return currRow * N + currCol
        
        if dp[length][currRow] != float('inf') and dp[length][currRow] < minPathHelper(currRow, dp[length][currRow], length - 1):
            return dp[length][currRow]
        
        if currRow < 0 or currRow >= N or currCol < 0 or currCol >= N:
            return float('inf')
        
        for neiRow, neiCol in [(currRow - 1, currCol), (currRow + 1, currCol), (currRow, currCol - 1), (currRow, currCol + 1)]:
            neiValue = grid[neiRow][neiCol]
            if neiValue < dp[length][currRow]:
                dp[length][currRow] = neiValue
                start[length] = (neiRow, neiCol)
                if length == k:
                    return neiValue
                minPathHelper(neiRow, neiCol, length - 1)
        
        return dp[length][currRow]
    
    result = minPathHelper(0, 0, k)
    if result == float('inf'):
        return []
    return [result // N + 1 for _ in range(k)] + [result // N + 1]