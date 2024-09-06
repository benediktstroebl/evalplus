
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
    nb_rows = len(grid)
    nb_cols = len(grid[0])
    buckets = nb_rows * [capacity]
    water_collected = 0
    operations = 0

    while True:
        operations += 1
        for col in range(nb_cols):
            # Collecting water from the row with highest water level
            highest_row = max(
                range(nb_rows),
                key=lambda row: grid[row][col] if grid[row][col] < buckets[row] else 0
            )
            if grid[highest_row][col] > 0:
                water_collected += grid[highest_row][col]
                grid[highest_row][col] = 0
                for row in range(nb_rows):
                    # Emptying the buckets
                    buckets[row] = min(buckets[row], water_collected)
                    # Filling the buckets
                    grid[row][col] = min(
                        grid[row][col] + buckets[row],
                        capacity
                    )
                    water_collected -= buckets[row]
            if water_collected == 0:
                return operations
