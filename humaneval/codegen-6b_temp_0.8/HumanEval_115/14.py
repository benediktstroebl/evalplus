
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
    
    n = len(grid)
    m = len(grid[0])
    buckets = 1
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                buckets *= grid[i][j]
    if buckets <= capacity:
        return 0
    
    # find each of the buckets that can be emptied
    bucket_indices = []
    bucket_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                bucket_indices.append((i,j))
                bucket_count += grid[i][j]
    bucket_indices = sorted(bucket_indices, key=lambda (row, col): grid[row][col], reverse=True)
    max_count = bucket_count
    
    # function to count number of moves
    def count_moves(buckets, capacity):
        bucket_capacity = capacity // buckets
        count = 0
        for i in range(buckets):
            if grid[bucket_indices[i][0]][bucket_indices[i][1]]:
                bucket_count = grid[bucket_indices[i][0]][bucket_indices[i][1]]
                bucket_capacity = capacity // bucket_count
                if bucket_capacity > 0:
                    count += bucket_capacity
                bucket_count -= 1
                grid[bucket_indices[i][0]][bucket_indices[i][1]] = bucket_count
        return count
    while bucket_count > 0:
        max_count = max(max_count, count_moves(buckets, bucket_capacity))
        buckets *= 2
        bucket_capacity //= 2
    return max_count