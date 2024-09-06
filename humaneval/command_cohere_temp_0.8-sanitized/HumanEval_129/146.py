def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Create a 2D list to store the shortest path and
    # an upwards-linked list to store the previous path
    path = [[0 for _ in range(N)] for _ in range(N)]
    prev_path = [None] * N

    start = 0
    end = N - 1

    # Initialize the first step of the shortest path
    path[start][0] = grid[start][0]
    prev_path[start] = [grid[start][0]]

    for _ in range(1, k):
        for i in range(N):
            # Find the smallest value in the adjacent cells
            mini = min(path[i][:-1], key=lambda x: x[0])[0]
            # Update the path if a smaller value is found
            if mini != path[i][-1]:
                path[i][-1] = mini
                prev_path[i] = mini

        start, end = end, start - 1 if end - start > 1 else 0

    # Reverse the list if the path is longer than k
    if end - start > 1:
        path = [row[::-1] for row in path]
        prev_path = [list(reversed(lst)) for lst in prev_path]

    return [p for i, p in enumerate(path[end]) if i == 0 or path[end][i - 1] != p]