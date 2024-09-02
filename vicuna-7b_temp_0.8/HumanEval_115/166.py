
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
    rows = grid.shape[0]
    cols = grid.shape[1]
    visited = [False] * (rows + 1) * (cols + 1)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                max_depth = 0
                max_bucket = 0
                for k in range(1, math.floor(min(i+1, rows-1))):
                    for l in range(1, math.floor(min(j+1, cols-1))):
                        if grid[k][l] == 1 and not visited[k][l]:
                            depth = max(depth, k-i-1)
                            bucket = max(bucket, k-j-1)
                            max_depth = max(max_depth, depth+bucket)
                bucket_index = math.ceil(max_depth / capacity)
                if bucket_index >= 0 and grid[i][j] == 1:
                    grid[i][j] = 0
                    bucket_index -= 1
                    for k in range(bucket_index):
                        for l in range(cols):
                            if visited[k][l] == False:
                                grid[k][l], bucket_index = max_fill(grid, capacity)
                                break
    return max_depth