
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
    def bucket_water(grid, capacity):
        #assuming n*n
        buckets = 1
        bucket_water = 0
        for row in grid:
            for el in row:
                if el == 1:
                    bucket_water += 1
            buckets += 1
        return [buckets, bucket_water]
    
    def can_fill(grid, bucket_water, bucket_capacity):
        for row in grid:
            if bucket_water - bucket_capacity >= len(row):
                return False
        return True

    def find_row(grid, bucket_water, bucket_capacity):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return i
    
    def find_column(grid, bucket_water, bucket_capacity, row):
        for i in range(len(grid[0])):
            if grid[row][i] == 1:
                return i
    
    def find_column_max(grid, bucket_water, bucket_capacity):
        max_water = 0
        for i in range(len(grid[0])):
            water = 0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    water += 1
            if water > max_water:
                max_water = water
        return max_water

    def fill_bucket(grid, bucket_water, bucket_capacity):
        bucket_water -= 1
        row = find_row(grid, bucket_water, bucket_capacity)
        column = find_column(grid, bucket_water, bucket_capacity, row)
        for i in range(len(grid)):
            if grid[i][column] == 1:
                bucket_water -= 1
        for i in range(row):
            if grid[i][column] == 1:
                bucket_water -= 1
        for i in range(len(grid)-1, row, -1):
            if grid[i][column] == 1:
