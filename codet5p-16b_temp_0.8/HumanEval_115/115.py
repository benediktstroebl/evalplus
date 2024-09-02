
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

    bucket_capacity = capacity
    n_rows, n_cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def fill_bucket(i, j, bucket_capacity):
        if not 0 <= i < n_rows or not 0 <= j < n_cols or grid[i][j] == 1 or (i, j) in visited:
            return 0
        visited.add((i, j))
        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
            fill_bucket(i+x, j+y, bucket_capacity)
        return bucket_capacity

    for i in range(n_rows):
        for j in range(n_cols):
            if (i, j) not in visited and grid[i][j] == 0:
                count += 1
                grid[i][j] = fill_bucket(i, j, bucket_capacity)
    return count


