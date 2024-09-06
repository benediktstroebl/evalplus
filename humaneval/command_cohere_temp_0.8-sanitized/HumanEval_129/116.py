def minPath(grid, k):
    N = len(grid)
    visited = [False] * N * N
    stack = []
    target = k

    while target > 0:
        min_row, min_col = None, None
        for i in range(N):
            for j in range(N):
                if not visited[i * N + j] and grid[i][j] != 0:
                    if min_row is None or grid[i][j] < min_row:
                        min_row, min_col = grid[i][j], j
                    elif grid[i][j] == min_row and j < min_col:
                        min_col = j

        visited[min_row * N + min_col] = True
        stack.append(min_row * N + min_col)
        target -= 1

    return stack[::-1]