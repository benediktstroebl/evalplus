
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

    def get_bucket(grid, bucket_capacity):
        import math
        m = len(grid)
        n = len(grid[0])
        bucket = [[math.inf for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bucket[i][j] = 0

        for i in range(m):
            for j in range(n):
                if j - 1 >= 0:
                    bucket[i][j] = min(bucket[i][j], bucket[i][j - 1] + 1)

        for j in range(n):
            for i in range(m):
                if i - 1 >= 0:
                    bucket[i][j] = min(bucket[i][j], bucket[i - 1][j] + 1)

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    bucket[i][j] =
