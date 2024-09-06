def minPath(grid, k):
    N = len(grid)
    if k > N:
        return []

    # Track visited and accumulated path values
    visited = [set() for _ in range(N)]
    acc_path = [[] for _ in range(N)]

    # Start from any cell
    start_idx = 0
    dir_graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                start_idx = i
                dir_graph[i] += [(0, j)]
                visited[i].add(j)
                acc_path[i] += [grid[i][j]]
                break

    # Track the minimum path and its length
    min_path = [None] * k
    min_path_len = float('inf')

    def dfs(curr_idx, curr_len):
        nonlocal min_path_len
        if curr_len == k:
            if min_path_len > curr_len:
                min_path_len = curr_len
                min_path = acc_path[curr_idx][:]
            return

        for dx, dy in dir_graph[curr_idx]:
            if (dx, dy) == (0, 0):
                continue  # Avoid moving off the grid

            next_idx = (curr_idx + dx) % N
            next_acc_path = acc_path[curr_idx] + [grid[next_idx][dy]]
            next_visited = visited[curr_idx].copy()
            next_visited.add(dy)

            if next_acc_path not in visited[next_idx]:
                dfs(next_idx, curr_len + 1)
                visited[next_idx].add(next_acc_path)

    dfs(start_idx, 0)

    # Return the minimum path
    return min_path[:k]
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
k = 3