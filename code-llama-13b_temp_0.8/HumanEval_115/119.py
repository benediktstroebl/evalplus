
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
    # A: bounds checking
    # B: start at the rightmost bottom most well
    # C: try to empty the well
    # D: if we cannot empty the well, move the bucket left
    # E: if the bucket is empty, move it up and try again
    # F: if we cannot empty the well, move the bucket up
    # G: if the bucket is full, move it left and try again
    # H: repeat until we cannot move the bucket
    # I: return how many times we moved the bucket
    rows = len(grid)
    cols = len(grid[0])
    # B: start at the rightmost bottom most well
    row = rows - 1
    col = cols - 1
    # C: try to empty the well
    num_operations = 0
    while row >= 0 and col >= 0:
        # D: if we cannot empty the well, move the bucket left
        while row >= 0 and col >= 0:
            # E: if the bucket is empty, move it up and try again
            while row >= 0:
                if grid[row][col] > 0:
                    # C: try to empty the well
                    break
                row -= 1
            # F: if we cannot empty the well, move the bucket up
            if row < 0:
                break
            # G: if the bucket is full, move it left and try again
            while col >= 0:
                grid[row][col] -= 1
                if grid[row][col] < 0:
                    break
                col -= 1
                num_operations += 1
            # H: repeat until we cannot move the bucket
            if col < 0:
                break
            row -= 1
            col += 1
        # I: return how many times we moved the bucket
        return num_operations
    
    
