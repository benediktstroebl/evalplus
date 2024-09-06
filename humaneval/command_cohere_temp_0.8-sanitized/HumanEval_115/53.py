import math
def max_fill(grid, capacity):
    """
    Uses buckets to empty wells efficiently.
    """
    rows, cols = len(grid), len(grid[0])
    if not rows * cols or not capacity:
        return 0

    # Combine rows to form a 2D matrix
    water = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            water[i][j] = grid[i][j]

    # Fill algorithm
    fills = 0
    buckets = 0
    for i in range(rows):
        prev_buckets = buckets
        for j in range(cols - capacity + 1):
            cur_buckets = math.ceil(water[i][j:j+capacity] / capacity)
            buckets += cur_buckets - prev_buckets
            fills = max(fills, buckets)

        water[i] = [min(water[i][j], capacity) for j in range(cols)]

    return fills