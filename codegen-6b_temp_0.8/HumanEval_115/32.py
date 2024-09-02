
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
    if grid is None or not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[0 for _ in row] for row in grid]
    nodes = [[(row, col) for col in range(cols)] for row in range(rows)]
    buckets = [[row, col] for col in range(cols) for row in range(rows) if grid[row][col]]

    def _calc_dist(x1, y1, x2, y2):
        return 1 + math.ceil((x1 - x2) / 2) + 1 + math.ceil((y1 - y2) / 2)

    def _add_to_bucket(node, bucket, visited):
        x, y = node
        visited[x][y] = 1
        bucket.append(node)

    def _has_water(node, water):
        x, y = node
        return grid[x][y] == 1 and grid[x - 1][y] == water and grid[x + 1][y] == water and grid[x][y - 1] == water and grid[x][y + 1] == water

    def _is_well_fully_filled(node):
        x, y = node
        return visited[x][y] == 1 and len(buckets) == 0 and capacity >= 0

    def _empty_well(node):
        x, y = node
        buckets.remove((x, y))
        visited[x][y] = 0

    def _del_well(node):
        x, y = node
        buckets.remove((x, y))
        visited[x][y] = 0

    def _find_max_dist(node):
        x, y = node
        max_dist = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    if 0 <= x + dx < rows and 0 <= y + dy < cols:
                        d = _calc_dist(x, y, x + dx, y + dy)
                        if d > max_dist: