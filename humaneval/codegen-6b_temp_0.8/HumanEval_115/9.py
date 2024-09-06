
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
    def import_grid(grid):
        # convert grid into a list of lists
        result = []
        for row in grid:
            result.append([])
            for e in row:
                result[-1].append(e)
        return result

    grid = import_grid(grid)
    # Horizontal search
    h = len(grid)
    # Vertical search
    w = len(grid[0])
    # Initialize the buckets
    result = 0
    # Search the well
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 1:
                # reduce capacity by 1
                grid[r][c] -= 1
                # if the bucket is empty
                if grid[r][c] < 0:
                    # increase result by 1
                    result += 1
                    # change the value of the bucket to current capacity
                    grid[r][c] += 1
    return result
