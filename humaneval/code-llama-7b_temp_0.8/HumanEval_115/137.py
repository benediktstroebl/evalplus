
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
    # 1. Take all wells which can be filled.
    # 2. Fill them with bucket and lower the bucket as much as possible.
    # 3. Once the bucket is full, extract all the water from the wells.
    # 4. Fill the wells with the remaining water.

    # 1. Find all the wells which can be filled.
    # 2. Fill the wells.
    # 3. Lower the bucket as much as possible.
    # 4. Extract all the water from the wells.
    # 5. Fill the wells with the remaining water.

    n = len(grid)
    if n == 0:
        return 0

    m = len(grid[0])
    if m == 0:
        return 0

    # Create a matrix for the buckets.
    bucket = [[0] * m for i in range(n)]

    # Count how many times we need to lower the bucket.
    times = 0

    # Fill the wells.
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                bucket[i][j] = 1

    # Fill the wells with the remaining water.
    while can_fill_more(bucket, capacity, n, m):
        for i in range(n):
            for j in range(m):
                if bucket[i][j] == 0:
                    continue
                elif bucket[i][j] < capacity:
                    bucket[i][j] += 1
                elif bucket[i][j] == capacity:
                    continue

        times += 1

    # Lower the bucket as much as possible.
    while can_lower_more(bucket, n, m):
        for i in range(n):
            for j in range(m):
                if bucket[i][j] > 0:
                    bucket[i][j] -= 1
        times += 1

    # Extract all the water from the wells.
    while can_extract_more(bucket, n, m):
