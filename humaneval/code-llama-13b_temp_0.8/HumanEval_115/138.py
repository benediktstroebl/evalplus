
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
    n = len(grid)
    m = len(grid[0])
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

    # Number of times to lower the buckets
    times = 0

    # Position of the buckets
    r, c = 0, m-1
    # Bucket direction
    dir = RIGHT
    while 1:
        # If direction is RIGHT, try to fill the bucket
        if dir == RIGHT:
            while c < m and grid[r][c] == 1:
                c += 1
            # If the bucket is filled, empty it
            if c < m:
                grid[r][c] = 0
                times += 1
            # If the bucket is empty, go back one position
            else:
                c -= 1
                # If the previous position is in the other direction, change the direction
                if dir == RIGHT:
                    dir = LEFT
                elif dir == LEFT:
                    dir = UP
                elif dir == UP:
                    dir = DOWN
                elif dir == DOWN:
                    dir = RIGHT
                    r += 1
        # If direction is LEFT, try to fill the bucket
        elif dir == LEFT:
            while c >= 0 and grid[r][c] == 1:
                c -= 1
            # If the bucket is filled, empty it
            if c >= 0:
                grid[r][c] = 0
                times += 1
            # If the bucket is empty, go back one position
            else:
                c += 1
                # If the previous position is in the other direction, change the direction
                if dir == RIGHT:
                    dir = LEFT
                elif dir == LEFT:
                    dir = UP
                elif dir == UP:
                    dir = DOWN
                elif dir == DOWN:
                    dir = RIGHT
                    r += 1
        # If direction is UP, try to fill the bucket
        elif dir == UP:
            while r >= 0 and grid[r][c] == 1:
                r -= 
