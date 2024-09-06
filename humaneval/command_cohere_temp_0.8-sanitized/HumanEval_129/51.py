def minPath(grid, k):
    n = len(grid)
    visited = [set() for _ in range(n)]
    stack = [(-1, -1)]  # (row, col)

    while stack and k:
        row, col = stack.pop()
        if k == 1:
            yield grid[row][col]
            break
        if k < 0:
            return

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n:
                if (new_row, new_col) not in visited[row]:
                    visited[row].add((new_row, new_col))
                    stack.append((new_row, new_col))
                    if len(visited[row]) == k:
                        yield from map(lambda c: grid[row][c], visited[row])
                        break

    if k > 0:
        return None