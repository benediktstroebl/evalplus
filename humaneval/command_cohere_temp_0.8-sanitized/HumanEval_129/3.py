def minPath(grid, k):
    n = len(grid)
    visited = [False] * (n * n)
    stack = []
    start = 0
    end = 0

    def dfs(i, j, prev_i, prev_j):
        nonlocal start, end

        if visited[get_index(i, j)] or (i < 0 or i >= n or j < 0 or j >= n):
            return

        visited[get_index(i, j)] = True

        if k == 1:
            stack.append(grid[i][j])
            return

        if not stack or (grid[i][j] < stack[-1][0] or (
            grid[i][j] == stack[-1][0] and (i, j) > stack[-1][1:]
        )):
            stack.append([grid[i][j], (i, j)])
            start, end = i, j

        for nei in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= nei[0] < n and 0 <= nei[1] < n:
                dfs(*nei, i, j)

    for i in range(n):
        for j in range(n):
            if not visited[get_index(i, j)]:
                dfs(i, j, -1, -1)

    res = [stack[0][0]]
    while stack and k > 1:
        val = stack.pop()[0]
        if val < res[-1]:
            res.append(val)
        else:
            break

    return res[1:]
def get_index(i, j):
    return i * n + j