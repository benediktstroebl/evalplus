
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
    def count_cap(x,y,cap):
        c = 0
        for i in range(x,x+row_length):
            for j in range(y,y+col_length):
                c += grid[i][j]
        return max(0,c-cap)
    row_length, col_length = len(grid[0]), len(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return 0
    results = []
    for row in grid:
        for index in range(len(row)):
            if row[index] == 0:
                results.append(count_cap(row,index,capacity))
    return sum(results)
