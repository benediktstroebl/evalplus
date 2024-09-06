
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

    def max_fill_h(grid, capacity, h):
        if capacity < 0 or h >= len(grid):
            return 0

        ans = max_fill_v(grid, capacity, 0, h)
        ans += max_fill_h(grid, capacity, h + 1)
        return ans
    
    def max_fill_v(grid, capacity, v, h):
        if capacity < 0 or v >= len(grid[h]):
            return 0

        if grid[h][v] == 0:
            return max_fill_v(grid, capacity, v + 1, h)
        else:
            ans = 0
            while v < len(grid[h]) and grid[h][v] != 0:
                capacity -= 1
                ans += 1
                v += 1

            ans += max_fill_h(grid, capacity, h + 1)
            return ans

    return max_fill_h(grid, capacity, 0)

