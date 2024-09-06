def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and last visited cells for each row and column
    visited = [[False] * (N * 2) for _ in range(N)]
    lastVisited = [[-1] * (N * 2) for _ in range(N)]

    def dfs(row, col, remaining):
        if remaining == 0:
            return grid[row][col]
        
        if visited[row][col] or grid[row][col] <= 0:
            return 0
        
        visited[row][col] = True
        lastVisited[row][col] = len(path)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < N and 0 <= newCol < N and not visited[newRow][newCol] and grid[newRow][newCol] > 0:
                nextVal = dfs(newRow, newCol, remaining - 1)
                if nextVal:
                    path.append(nextVal)
                    lastVisited[newRow][newCol] = len(path) - 1
                    return nextVal
        
        return 0

    path = []
    startCol = 0
    startRow = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > 0:
                startRow, startCol = i, j
                break
    
    return [grid[startRow][startCol]] + dfs(startRow, startCol, k - 1)