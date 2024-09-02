
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

    def get_gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    rows = len(grid)
    cols = len(grid[0])

    if capacity > cols:
        return rows * cols

    gcd = get_gcd(rows, cols)
    if capacity < gcd:
        return -1

    bucket_count = math.ceil(rows / capacity)
    bucket_count *= math.ceil(cols / capacity)

    low = 0
    high = rows * cols

    while low < high:
        mid = (low + high) // 2

        filled_wells = 0
        for row in range(rows):
            for col in range(cols):
                filled_wells += (
                    grid[row][col] - (row // capacity) * (col // capacity)
                ) // mid

        if filled_wells < bucket_count:
            high = mid
        else:
            low = mid + 1
    return low - 1
