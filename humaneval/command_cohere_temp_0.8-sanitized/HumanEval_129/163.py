def minPath(grid, k):
    n = len(grid)
    visited = [set() for _ in range(n)]
    stack = []
    start = 0
    while stack <= k and start < n * n:
        row, col = divmod(start, n)
        if not (row, col) in visited[row]:
            visited[row].add((row, col))
            stack += 1
            if stack == k:
                return [grid[row][col]] * k
            for nei in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
                if 0 <= nei[0] < n and 0 <= nei[1] < n and nei != (row, col) and (nei[0], nei[1]) not in visited[row]:
                    start = (nei[0] * n + nei[1])
        else:
            i = start // n
            j = start % n
            start = min((i + x) * n + j for x in (-1, 0, 1) if (i + x) in visited[i] and (j + x) in visited[j])
    return []