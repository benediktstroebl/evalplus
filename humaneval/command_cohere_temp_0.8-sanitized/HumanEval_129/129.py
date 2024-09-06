def minPath(grid, k):
    N = len(grid)
    def dfs(r, c, path, visited, prev_path):
        if len(path) == k:
            return path if prev_path is None or sorted(path) < sorted(prev_path) else prev_path
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newR, newC = r + dr, c + dc
            if 0 <= newR < N and 0 <= newC < N and grid[newR][newC] != 0 and (newR, newC) not in visited:
                visited.add((newR, newC))
                temp_path = dfs(newR, newC, path + [grid[newR][newC]], visited, prev_path)
                if temp_path:
                    return temp_path
        return None

    visited = set()
    return dfs(0, 0, [], visited, None)