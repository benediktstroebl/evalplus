
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
    def floor_sqrt(n):
        return int(math.sqrt(n))

    def find_max_pour(grid, i, j):
        """
        @return: How much water can be poured out from the ith row and jth column
        """
        i_max = 0
        j_max = 0
        if i == 0:
            i_max = floor_sqrt(j)
        else:
            i_max = floor_sqrt(i * j)
        
        if j == 0:
            j_max = floor_sqrt(i)
        else:
            j_max = floor_sqrt(i * j)

        return i_max * j_max

    def water_trapped(grid, n, m, bucket_capacity):
        n = len(grid)
        m = len(grid[0])

        # make m*n matrix to store maximum water
        # at each point in the grid
        max_water = [[0 for x in range(m)] for y in range(n)]

        # maximum water in bottom row considered as
        # reference point to find maximum water
        for j in range(m-1, 0, -1):
            max_water[n-1][j] = grid[n-1][j]

        # maximum water in rightmost column considered as
        # reference point to find maximum water
        for i in range(n-2, -1, -1):
            max_water[i][m-1] = grid[i][m-1]

        # maximum water in bottom right corner considered as
        # reference point to find maximum water
        i = n-1
        j = m-1
        while i > 0 and j > 0:
            pour = find_max_pour(grid, i, j)
            max_water[i][j] = min(pour, bucket_capacity)
            if pour == bucket_capacity:
                break
            i -= 1
            j -= 1

        # update water trapped
        water_trapped = 0
        for i in range(n):
            for j in range(
