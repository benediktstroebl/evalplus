
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    # Time: O(rows * cols)
    # Space: O(rows * cols)

    wells = []
    for row_index in range(len(grid)):
        well = []
        for col_index in range(len(grid[0])):
            if grid[row_index][col_index] == 1:
                well.append(row_index * len(grid[0]) + col_index)
        wells.append(well)

    def dijkstra(s, t):
        dist = [-1] * len(grid)
        dist[s] = 0
        visited = set()
        queue = [(0, s)]
        while len(queue) != 0:
            curr_dist, curr_node = queue.pop(0)
            if curr_node == t:
                return curr_dist
            visited.add(curr_node)
            for next_node in wells[curr_node]:
                if next_node not in visited:
                    dist_to_next = curr_dist + 1
                    if dist[next_node] == -1 or dist[next_node] > dist_to_next:
                        dist[next_node] = dist_to_next
                        queue.append((dist_to_next, next_node))
        return dist[t]

    def count_moves(capacity):
        moves = 0
        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                if grid[row_index][col_index] == 1:
                    if dijkstra(row_index * len(grid[0]) + col_index, 0) == -1:
                        moves += 1
        return moves

    low = 0
    high = 10
    while low < high:
        mid = math.floor((low + high) / 2)
        if count_moves(mid) <= capacity:
            low = mid + 1
        else:
            high = mid - 1
    return high

