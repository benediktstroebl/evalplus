
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
    wells_left = set()
    wells_right = set()
    bucket_capacity = capacity
    total_fills = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                wells_left.add(row)
                wells_right.add(col)

    while bucket_capacity > 0 and wells_left and wells_right:
        bucket_capacity -= 1
        max_left = -math.inf
        max_right = -math.inf

        for row in wells_left:
            if row > max_left:
                max_left = row

        for col in wells_right:
            if col > max_right:
                max_right = col

        for row in wells_left:
            if row == max_left:
                wells_left.remove(row)
                break

        for col in wells_right:
            if col == max_right:
                wells_right.remove(col)
                break

        total_fills += 1

    return total_fills

