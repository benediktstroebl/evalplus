def minPath(grid, k):
    N = len(grid)
    visited = [False] * (N * N)
    stack = []
    dist = [float('inf')] * (N * N)
    dist[grid[0][0]] = 0
    stack.append(grid[0][0])
    while len(stack) > 0:
        curr = stack.pop()
        visited[curr] = True
        for nei in range(N):
            nei_row, nei_col = curr % N, curr // N
            nei_pos = nei_row * N + nei_col
            if not visited[nei_pos]:
                if dist[nei_pos] > dist[curr] + 1:
                    dist[nei_pos] = dist[curr] + 1
                    stack.append(nei_pos)
    path = [pos for pos in range(N * N) if dist[pos] == k - 1 and visited[pos]]
    return path