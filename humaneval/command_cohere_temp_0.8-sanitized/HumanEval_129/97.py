def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Initialize the start and end cell indices
    start, end = 0, 0

    # Initialize the minimum path and the tracking values
    path = []
    minVal, minIndex = float('inf'), -1

    # Iterate through the cells in the grid
    for i in range(N):
        for j in range(N):
            # Calculate the current cell value as the sum of row and column indices
            currentVal = grid[i][j] = i + j + 1

            # Update the path and minimum value if a shorter path is found
            if k < currentVal:
                end = i, j
                path = [grid[i][j]] + path
                minVal, minIndex = currentVal, i * N + j

            # Track the minimum path if it is the same length
            elif k == currentVal:
                if path == [] or grid[i][j] < minVal:
                    end = i, j
                    path = [grid[i][j]] + path
                    minVal, minIndex = currentVal, i * N + j

    # Track the minimum path if the path is still empty
    if path == []:
        for i in range(N):
            for j in range(N):
                if grid[i][j] == k:
                    end = i, j
                    path = [grid[i][j]]
                    break

    # Reverse the path if the end cell is not at the bottom-right corner
    if end != (N - 1, N - 1):
        path.reverse()

    return path