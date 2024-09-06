def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    def dfs(r, c, path, visited, prev):
        if len(path) == k:
            return True, path

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newR, newC = r + dr, c + dc
            if 0 <= newR < N and 0 <= newC < N and grid[newR][newC] > prev and not visited[newR][newC]:
                visited[newR][newC] = True
                if dfs(newR, newC, path, visited, grid[newR][newC]):
                    return True, path + [grid[newR][newC]]
                visited[newR][newC] = False

        return False, path

    visited = [[False] * N for _ in range(N)]
    prev = float('-inf')
    ans = []
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and grid[r][c] > prev:
                prev = grid[r][c]
                if dfs(r, c, [], visited, prev):
                    ans = max(ans, [], key=len)
                    ans.append(prev)
                    break
    return ans