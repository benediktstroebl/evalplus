
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
    unique_row = []
    for row in grid:
        if row not in unique_row:
            unique_row.append(row)

    unique_column = [column[0] for column in grid.T]
    unique_column = sorted(list(set(unique_column)))

    # Calculate the number of times the buckets have to be lowered to empty by combinations of wells and bucket
    # capacity.
    result = math.factorial(len(unique_row))
    result *= math.factorial(len(unique_row))
    result *= math.factorial(len(unique_column))
    result *= math.factorial(len(unique_column))

    return result
