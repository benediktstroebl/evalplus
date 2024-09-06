def minPath(grid, k):
    N = len(grid)
    visited = [set() for _ in range(N)]
    stack = [(-1, -1)]  # (-1, -1) represents the starting cell

    while stack:
        cell = stack.pop()
        i, j = cell
        if k == 1:
            return [grid[i][j]] if i != -1 and j != -1 else []

        if (i, j) not in visited[i] and k >= 1:
            visited[i].add((i, j))
            stack.append((i - 1, j))
            stack.append((i + 1, j))
            stack.append((i, j - 1))
            stack.append((i, j + 1))
            k -= 1

    return []
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
k = 3