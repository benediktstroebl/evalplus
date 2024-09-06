
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
    if len(grid) == 0:
        return 0

    grid = [list(map(int, list(row))) for row in grid]
    n, m = len(grid), len(grid[0])
    r, c = n - 1, m - 1
    height_map = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            height_map[i][j] = grid[i][j]
            if j < c:
                height_map[i][j] += height_map[i][j + 1]
            if i < r:
                height_map[i][j] += height_map[i + 1][j]

    def calc_h(i, j, grid, capacity):
        """
        Calculate the height.
        """
        height = 0
        while i < n and j < m and grid[i][j]:
            height += 1
            i, j = i + height, j + 1
        return height

    def calc_heigh(i, j, grid, capacity):
        """
        Calculate the height.
        """
        height = 0
        while i < n and j < m and grid[i][j]:
            height += 1
            i, j = i + height, j + 1
        return height

    def calc_pour(i, j, grid, capacity, height_map):
        """
        Calculate the number of pours.
        """
        height = calc_h(i, j, grid, capacity)
        if height <= capacity:
            return 0

        if height_map[i][j] >= height:
            return math.ceil(height / capacity) - 1
        else:
            return math.ceil(height / capacity)

    # find the maximum height in the grid.
    height_map = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            height_map[i][j] = calc_h(i
