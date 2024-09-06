
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
    # Fill out this code
    """
    This is a greedy algorithm that minimizes the number of bucket rounds needed to fill a rectangular grid of wells.
    The idea is to start filling the grid from the top-left corner and proceed in a row-by-row manner, always
    filling the wells with the smallest amount of water needed to reach the required capacity.
    This is done by keeping track of the amount of water needed to fill each well, as well as the number of buckets
    needed to fill each row of wells.
    The algorithm then proceeds to the next row of wells, always filling the wells with the smallest amount of water
    needed to reach the required capacity, until all rows of wells have been filled.
    The number of bucket rounds needed to fill the entire grid is the minimum number of rounds needed to fill the
    top-left corner of the grid, plus the number of rounds needed to fill the rest of the grid.
    """
    current_round = 0
    row = 0
    while row < len(grid):
        current_round += 1
        if current_round > capacity:
