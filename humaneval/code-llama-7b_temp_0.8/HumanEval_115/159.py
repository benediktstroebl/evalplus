
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

    # Flatten the grid
    wells = list(i for j in grid for i in j)
    wells_len = len(wells)

    # Make a copy of wells
    # Pop out the zeros from the copy
    # If the copy is empty, return the original
    # Else, call max_fill(copy)
    # For each 1 in the copy, subtract it from the original
    # If the capacity is met, return 1 plus the result from the copy
    # Else, return 0 plus the result from the copy

    bucket_capacity = 1
    result = max_fill(grid, capacity)

    if result == wells_len:
        return 0

    for i in range(result, wells_len):
        wells[i] -= 1
        if wells[i] == 0:
            wells.pop(i)
            wells_len -= 1
        else:
            break
    
    if wells_len == 0:
        return result
    
    return result + max_fill(wells, capacity)
