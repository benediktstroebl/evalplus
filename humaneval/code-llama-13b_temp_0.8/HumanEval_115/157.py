
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
    max_wells = int(math.ceil((capacity + 1) / 2))
    minimum_fills = capacity
    minimum_fills_total = 0

    for row in range(rows):
        # This is to keep the row in sync with the right well.
        j = max_wells - 1
        for col in range(cols):
            # This is to keep the column in sync with the top well.
            i = max_wells - 1
            while i >= 0 and j >= 0:
                if grid[row][col] >= i + j:
                    minimum_fills = min(minimum_fills, i + j)
                    i -= 1
                    j -= 1
                else:
                    j -= 1
            minimum_fills = capacity
        minimum_fills_total += minimum_fills
    return minimum_fills_total

