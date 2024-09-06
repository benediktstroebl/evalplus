def minPath(grid, k):
    N = len(grid)
    visited = [False] * (N * N)
    stack = []
    start = 0
    end = 0
    direction = [0, 0]

    def dfs(current):
        global start, end, direction
        if visited[current]:
            return False, 0, 0
        visited[current] = True
        stack.append(current)
        if len(stack) == k:
            end = current
            return True, 0, 0
        row, col = ord(grid[0][0]) - 96, ord(grid[0][1]) - 64
        for i in range(N):
            for j in range(N):
                if grid[i][j] != ' ':
                    nei = (row + i, col + j)
                    if not visited[nei] and dfs(nei):
                        start, end, direction = nei, current, nei - current
                        return True, i, j
    if dfs(0):
        if direction == [0, 0]:
            return [grid[start][0], grid[start][1]]
        return [grid[start][direction[0]], grid[start][direction[1]]]
    return [grid[end][0], grid[end][1]]