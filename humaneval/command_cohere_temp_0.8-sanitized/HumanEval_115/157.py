import math
import collections
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
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
    rows_with_water = collections.Counter(row for row in grid if len(row) and row[0] == 1)
    columns_with_water = collections.Counter(row for row in grid if row[0] == 1)
    
    count = 0
    for row in rows_with_water:
        max_row_fill = math.floor(capacity / rows_with_water[row])
        min_column_fill = capacity - max_row_fill * rows_with_water[row]
        
        for col in columns_with_water:
            if columns_with_water[col] > min_column_fill:
                count += 1
                break
    
    return count