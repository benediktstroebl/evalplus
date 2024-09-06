def minPath(grid, k):
    n = len(grid)
    if k > n * n or k <= 0:
        return []

    # Create a 2D list to store the paths up to length k
    dp = [[[0] * (n * n + 1) for _ in range(k + 1)] for _ in range(n + 1)]

    start_node = [i for i in range(n + 1)] * n
    end_node = [i for i in range(n + 1)] * n
    node_id = [[] for _ in range(n * n + 1)]

    # Helper function to get the node index
    def get_index(row, col):
        return row * n + col

    # Helper function to get the node value
    def get_value(row, col):
        return grid[row][col]

    # Fill the initial paths
    for row in range(n):
        for col in range(n):
            node_id[get_index(row, col)].append((row, col))
            dp[row][0][get_value(row, col)] = 1

    # Build the dp values
    for length in range(1, k + 1):
        for row in range(n):
            for col in range(n):
                for nei in node_id[get_index(row, col)]:
                    nei_row, nei_col = nei
                    if nei_row > row or nei_col > col:
                        continue
                    dp[row][length][get_value(nei_row, nei_col)] = min(
                        dp[row][length][get_value(nei_row, nei_col)],
                        dp[row][length - 1][get_value(row, col)] + 1
                    )

    # Find the minimum path end node
    min_path = []
    start_node_id = node_id[get_index(*start_node)]
    end_node_id = node_id[get_index(*end_node)]
    for length in range(k, -1, -1):
        for node in start_node_id:
            if dp[node[0]][length][get_value(node[0], node[1])] == length:
                min_path.append(get_value(node[0], node[1]))
                if node in end_node_id:
                    break
    return min_path[::-1]