
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
    #Initialization
    n = len(grid)
    m = len(grid[0])
    # print(n)
    # print(m)
    if n*m < capacity:
        return 0
    # print(grid)
    # print(capacity)

    # Functions
    # Check for water
    def is_water(i,j):
        # print(i,j)
        if grid[i][j] == 1:
            # print('YES')
            return 1
        else:
            # print('NO')
            return 0
    
    # Check for water in the row
    def is_water_row(i):
        # print(i)
        # print('row')
        for j in range(m):
            if grid[i][j] == 1:
                # print('YES')
                return 1
        # print('NO')
        return 0

    # Check for water in the column
    def is_water_col(j):
        # print(j)
        # print('col')
        for i in range(n):
            if grid[i][j] == 1:
                # print('YES')
                return 1
        # print('NO')
        return 0

    # Check for water in the row
    def is_water_row_counter(i):
        # print(i)
        # print('row')
        count = 0
        for j in range(m):
            if grid[i][j] == 1:
                # print('YES')
                count+=1
        # print('NO')
        return count

    # Check for water in the column
    def is_water_col_counter(j):
        # print(j)
        # print('col')
        count = 0
        for i in range(n):
            if grid[i][j] == 1:
                # print('YES')
                count+=1
        # print('NO')
        return count
    
    def max_counter():
        max_count = 0
        for i in range(n):
            for j in range(m):
