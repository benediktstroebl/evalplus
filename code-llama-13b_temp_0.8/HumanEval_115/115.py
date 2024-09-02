
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
    cols = len(grid[0])
    bucket = capacity
    moves = 0
    if not rows:
        return moves
    # Find the first row with a 1
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                break
        # If we find a row with a 1, fill it up.
        if grid[row][col] == 1:
            break
    # We have a row with a 1, so we need to find the first row that does not have a 1.
    for next_row in range(row+1, rows):
        if 1 not in grid[next_row]:
            break
    # If the first row that does not have a 1 is less than or equal to the current row,
    # we have exhausted all the rows.
    if next_row == row:
        return moves
    # We have at least one row with a 1 and at least one row without a 1, so fill up the current row.
    if not bucket >= cols - col:
        raise ValueError("Capacity is too small for the grid")
    moves += math.ceil((cols - col) / bucket) * bucket
    # Fill the buckets to the correct height for the next row.
    moves += (next_row - row - 1) * bucket
    # Recurse to fill up the rest of the rows.
    moves += max_fill(grid[next_row:], bucket)
    return moves

