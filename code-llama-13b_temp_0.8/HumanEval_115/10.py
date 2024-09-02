
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
    max_row = 0
    n_cols = len(grid[0])
    for i, row in enumerate(grid):
        if sum(row) > 0:
            max_row = i
    max_row += 1
    n_rows = max_row
    # Too many columns or rows.
    if n_cols > n_rows:
        grid = list(map(list, zip(*grid)))
        n_rows = len(grid)
        n_cols = max_row

    total_rows = len(grid)
    total_cols = len(grid[0])

    # Create the graph.
    graph = {}
    # Create the verticals.
    for c in range(total_cols - 1):
        # Add the source.
        source = total_rows * c
        graph[source] = {}
        # Add the vertices.
        for r in range(total_rows):
            graph[source][source + r + 1] = grid[r][c]
        # Add the sink.
        sink = source + total_rows
        graph[source][sink] = 0
        # Add the edges.
        for r in range(total_rows - 1):
            graph[source + r + 1][source + r + 2] = grid[r][c]
        # Add the last vertex.
        if c + 1 != total_cols - 1:
            graph[source + total_rows][source] = 0
    # Create the horizontals.
    for r in range(total_rows - 1):
        # Add the source.
        source = (total_cols - 1) * r
        graph[source] = {}
        # Add the vertices.
        for c in range(total_cols):
            graph[source][source + c + 1] = grid[r][c]
        # Add the sink.
        sink = source + total_cols
        graph[source][sink] = 0
        # Add the edges.
        for c in range(total_cols - 1):
            graph[source + c + 1][source + c + 2] = grid[r
