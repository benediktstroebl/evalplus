
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
    row = len(grid)
    col = len(grid[0])
    # Search for all the starting points
    start_point = []
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                start_point.append([i, j])
    max_count = 0
    if len(start_point) == 0:
        return 0
    # Use BFS to find all the possible routes
    for sp in start_point:
        q = deque()
        q.append(sp)
        visited = [[False for i in range(col)] for j in range(row)]
        visited[sp[0]][sp[1]] = True
        count = 0
        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur[0] == row - 1 and cur[1] == col - 1:
                    return count
                for nxt in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if cur[0] + nxt[0] < 0 or cur[0] + nxt[0] >= row or cur[1] + nxt[1] < 0 or cur[1] + nxt[1] >= col:
                        continue
                    if grid[cur[0] + nxt[0]][cur[1] + nxt[1]] == 0:
                        continue
                    if visited[cur[0] + nxt[0]][cur[1] + nxt[1]]:
                        continue
                    q.append([cur[0] + nxt[0], cur[1] + nxt[1]])
                    visited[cur[0] + nxt[0]][cur[1] + nxt[1]] = True
            count += 1
        max_count = max(max_count, count)
    return max_count


