
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
    def solve(grid, capacity):
        m, n = len(grid), len(grid[0])
        # put all the water in one bucket
        queue = []
        bucket = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j, 0))
        while queue:
            i, j, count = queue.pop(0)
            if count > capacity:
                continue
            if i - 1 >= 0 and grid[i - 1][j]:
                bucket[i][j] = count + 1
                queue.append((i - 1, j, bucket[i][j]))
            if i + 1 < m and grid[i + 1][j]:
                bucket[i][j] = count + 1
                queue.append((i + 1, j, bucket[i][j]))
            if j - 1 >= 0 and grid[i][j - 
