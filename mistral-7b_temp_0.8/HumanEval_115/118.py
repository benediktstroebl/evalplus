
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
    def is_free(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
            return True
        return False

    def max_fill_recur(grid, capacity, x, y):
        if not is_free(x, y):
            return 0
        if capacity == 0:
            return 0

        water = 0
        water += max_fill_recur(grid, capacity - 1, x, y - 1) # go left
        water += max_fill_recur(grid, capacity - 1, x, y + 1) # go right
        water += max_fill_recur(grid, capacity - 1, x - 1, y) # go up
        water += max_fill_recur(grid, capacity - 1, x + 1, y) # go down

        water += 1

        return water

    return max_fill_recur(grid, capacity, 0, 0)

