
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
    rows, cols = len(grid), len(grid[0])
    h_buckets = [[0]*cols for _ in range(rows)]
    v_buckets = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r == 0:
                h_buckets[r][c] = grid[r][c]
                h_buckets[r][c] += h_buckets[r][c-1] if c > 0 else 0
            else:
                h_buckets[r][c] = h_buckets[r-1][c]
                h_buckets[r][c] += grid[r][c]
                h_buckets[r][c] += h_buckets[r][c-1] if c > 0 else 0
    
    for c in range(cols):
        for r in range(rows):
            if c == 0:
                v_buckets[r][c] = grid[r][c]
                v_buckets[r][c] += v_buckets[r-1][c] if r > 0 else 0
            else:
                v_buckets[r][c] = v_buckets[r][c-1]
                v_buckets[r][c] += grid[r][c]
                v_buckets[r][c] += v_buckets[r-1][c] if r > 0 else 0

    # Check for every well if it can be filled from a bucket
    # This can be achieved if the h and v bucket sums are equal or less than the well capacity
    # If it can be filled, the difference will be equal to the well capacity.
    # Otherwise, a new bucket will be needed to fill the well
    min_buckets = min(sum(row) for row in h_buckets)
    max_buckets = max(sum(row) for row in h_buckets)
    result = math.ceil(max_buckets/capacity)
    if min_buckets <= capacity:
        result = max(result, math.ceil(min_buckets/capacity))
    else:
        result = max(result, 1)

    min_buckets = min(sum(row) for row in v_buckets)
    max_buckets = max(sum(row) for row in v_buckets)
    if min_buckets <= capacity
