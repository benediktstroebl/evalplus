
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
    total_rows = n
    total_columns = m
    # print(f'total_rows: {total_rows}, total_columns: {total_columns}')

    # calculate the sum of each row
    sum_of_each_row = [0] * n
    for i in range(n):
        for j in range(m):
            sum_of_each_row[i] += grid[i][j]

    # calculate the sum of each column
    sum_of_each_column = [0] * m
    for i in range(n):
        for j in range(m):
            sum_of_each_column[j] += grid[i][j]

    #print(f'sum_of_each_row: {sum_of_each_row}, sum_of_each_column: {sum_of_each_column}')

    # calculate the number of times you need to lower the buckets 
    times = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                row_sum = sum_of_each_row[i] - grid[i][j]
                column_sum = sum_of_each_column[j] - grid[i][j]
                #print(f'row_sum: {row_sum}, column_sum: {column_sum}')
                if row_sum <= capacity and column_sum <= capacity:
                    times += 1
                elif row_sum > capacity and column_sum <= capacity:
                    times += math.ceil(row_sum / capacity)
                elif row_sum <= capacity and column_sum > capacity:
                    times += math.ceil(column_sum / capacity)
                else:
                    times += math.ceil(row_sum / capacity) + math.ceil(column_sum / capacity)
    
    return times
