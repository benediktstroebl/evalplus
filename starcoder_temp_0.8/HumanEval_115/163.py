
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

    # build graph
    graph = defaultdict(set)
    num_rows = len(grid)
    num_cols = len(grid[0])
    for row, row_value in enumerate(grid):
        for col, col_value in enumerate(row_value):
            # possible neighbors
            if row > 0: # top row
                graph[row*num_cols + col].add(row*num_cols + col-num_cols)
            if row < num_rows-1: # bottom row
                graph[row*num_cols + col].add(row*num_cols + col+num_cols)
            if col > 0: # left column
                graph[row*num_cols + col].add((row-1)*num_cols + col)
            if col < num_cols-1: # right column
                graph[row*num_cols + col].add((row+1)*num_cols + col)
    
    # BFS
    visited = set()
    max_level = math.ceil(num_rows*num_cols / capacity)
    level = 0
    bfs_queue = deque([0])
    while len(bfs_queue) > 0 and level < max_level:
        level += 1
        size = len(bfs_queue)
        for _ in range(size):
            current = bfs_queue.popleft()
            visited.add(current)
            if len(visited) == num_rows*num_cols:
                return level
            for neighbor in graph[current]:
                if neighbor not in visited:
                    bfs_queue.append(neighbor)

    return -1
