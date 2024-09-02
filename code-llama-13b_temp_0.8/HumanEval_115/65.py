
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
    rows = len(grid)
    columns = len(grid[0])
    dp = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    dp[rows][columns] = math.inf

    def fill_water(row, column, amount):
        if row < rows and column < columns:
            if grid[row][column] >= 1:
                amount = min(amount, grid[row][column])
            dp[row][column] = amount
            if row > 0:
                fill_water(row - 1, column, amount)
            if column > 0:
                fill_water(row, column - 1, amount)
            if row < rows:
                fill_water(row + 1, column, amount)
            if column < columns:
                fill_water(row, column + 1, amount)

    fill_water(0, 0, capacity)

    result = 0
    for i in range(0, rows):
        for j in range(0, columns):
            result += (capacity - dp[i + 1][j + 1])

    return result
