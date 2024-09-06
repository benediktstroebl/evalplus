def minPath(grid, k):
    N = len(grid)
    visited = [False] * (N * N)
    stack = []
    start = 0
    end = 0
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(current, goal):
        nonlocal start, end
        
        if visited[current] or current == goal:
            return
        visited[current] = True
        stack.append(current)
        for dx, dy in direction:
            new_x, new_y = current[0] + dx, current[1] + dy
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_x][new_y] != 0 and not visited[new_x + N * new_y] and dfs(new_x + N * new_y, goal):
                start = stack.pop()
                end = new_x + N * new_y
                return

    for i in range(N):
        for j in range(N):
            if not visited[i + N * j] and grid[i][j] != 0:
                dfs(i + N * j, i + N * N - 1)
                if len(stack) == k:
                    return [grid[a][b] for a, b in zip(start, end)]
    
    return []