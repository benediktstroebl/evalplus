
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

    def is_filled(x, y):
        return grid[y][x] == 1
    m, n = len(grid), len(grid[0])
    seen = {}
    def get_visited_count(x, y):
        key = (x, y)
        if key in seen:
            return seen[key]

        num_filled = 0
        if x >= 1 and is_filled(x-1, y):
            num_filled += 1 + get_visited_count(x-1, y)
        if y >= 1 and is_filled(x, y-1):
            num_filled += 1 + get_visited_count(x, y-1)
        if x < n-1 and is_filled(x+1, y):
            num_filled += 1 + get_visited_count(x+1, y)
        if y < m-1 and is_filled(x, y+1):
            num_filled += 1 + get_visited_count(x, y+1)

        seen
