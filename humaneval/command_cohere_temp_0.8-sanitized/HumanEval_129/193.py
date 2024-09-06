def minPath(grid, k):
    n = len(grid)
    visited = set()
    queue = [(0, 0)]  # starting cell (row, col)

    while queue and k:
        row, col = queue.pop()
        visited.add((row, col))
        k -= 1

        for nei in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
            if 0 <= nei[0] < n and 0 <= nei[1] < n and grid[nei[0]][nei[1]] != 0 and (nei[0], nei[1]) not in visited:
                queue.append(nei)
    
    return [grid[row][col] for row, col in visited]