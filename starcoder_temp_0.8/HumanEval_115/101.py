
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
    
    def _fill_grid(grid, row, col, cap):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False

        if grid[row][col] == 0:
            return False

        if cap == 0:
            return True

        grid[row][col] = 0

        if _fill_grid(grid, row + 1, col, cap - 1):
            return True
        if _fill_grid(grid, row - 1, col, cap - 1):
            return True
        if _fill_grid(grid, row, col + 1, cap - 1):
            return True
        if _fill_grid(grid, row, col - 1, cap - 1):
            return True

        grid[row][col] = 1
        return False


    empty_wells = 0
    # Find empty wells
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                empty_wells += 1

    # Fill wells from bottom to top
    empty_wells = empty_wells // capacity
    cap_wells = empty_wells * capacity
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                if _fill_grid(grid, row, col, cap_wells):
                    empty_wells -= 1

    return empty_wells

