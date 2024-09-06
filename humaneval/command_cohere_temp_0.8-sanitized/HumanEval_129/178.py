def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, tracker):
        if len(path) == k:
            return True  # Found a valid path of length k

        if visited[r][c]:
            return False  # Already visited

        visited[r][c] = True

        # Explore each of the 4 possible directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newR, newC = r + dr, c + dc
            if 0 <= newR < N and 0 <= newC < N:
                if grid[newR][newC] == tracker:
                    if dfs(newR, newC, path, visited, grid[newR][newC]):
                        return True
                elif grid[newR][newC] < tracker:
                    path.append(grid[newR][newC])
                    if dfs(newR, newC, path, visited, grid[newR][newC]):
                        return True

        return False  # Reached end of a dead-end branch, backtrack

    if k <= 0 or k > N * N:
        return []  # Invalid input

    path = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    tracker = grid[0][0]
    if dfs(0, 0, path, visited, tracker):
        return list(reversed(path))
    else:
        return []