def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and min path indices
    visited = [False] * (N * N)
    minPathIndices = [-1] * (N * N)
    stack = []
    stack.append(0)  # Start from the first cell

    while stack:
        cell = stack.pop()
        visited[cell] = True

        if k == 1:
            minPathIndices[cell] = 0
            return [grid[cell // N][cell % N]]

        for neighbor in range(N * N):
            if not visited[neighbor] and (grid[cell // N][cell % N] < grid[neighbor // N][neighbor % N] or
                                             minPathIndices[neighbor] == -1):
                stack.append(neighbor)
                minPathIndices[neighbor] = cell + 1

    # Reconstruct the min path
    result = []
    i = len(visited) - 1
    while i >= 0:
        while i < len(visited) - 1 and not visited[i + 1]:
            i += 1
        result.append(grid[minPathIndices[i] // N][minPathIndices[i] % N])
        i = minPathIndices[i] - 1
    return result[::-1]