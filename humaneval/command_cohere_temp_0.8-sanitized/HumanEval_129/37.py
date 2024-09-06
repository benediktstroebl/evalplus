def minPath(grid, k):
    n = len(grid)
    visited = [False] * (n * n)
    stack = []
    start = 0
    end = 0
    direction = [0, 0]

    def dfs(current):
        nonlocal start, end, direction
        if visited[current]:
            return False, []

        visited[current] = True
        stack.append(current)
        direction = [0, 0]

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0 and not visited[current + (i + direction[0]) * n + (j + direction[1])] and \
                        (start == 0 or grid[i][j] < grid[start][0]) and \
                        (end == 0 or grid[i][j] > grid[end][0]):
                    if dfs(current + (i + direction[0]) * n + (j + direction[1]))[0]:
                        start = i
                        end = j
                        return True, []
                    elif not dfs(current + (i - direction[0]) * n + (j - direction[1]))[0]:
                        start = i
                        end = j
                        return False, []
                    direction[0] = -direction[0]
                    direction[1] = -direction[1]

    result = []
    if dfs(0)[0]:
        for _ in range(k):
            result.append(grid[start][end])
            if start > 0:
                start -= 1
            else:
                start = n - 1
            if end < n - 1:
                end += 1
            else:
                end = 0
    return result[::-1]