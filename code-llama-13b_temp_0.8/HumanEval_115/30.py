
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

    def find_min_fill(start_row, start_col, capacity):
        if capacity == 0:
            return 0, 0, 0

        if capacity < 0:
            return math.inf, -1, -1

        if start_row < 0 or start_row >= len(grid):
            return math.inf, -1, -1

        if start_col < 0 or start_col >= len(grid[0]):
            return math.inf, -1, -1

        if grid[start_row][start_col] == 0:
            return math.inf, -1, -1

        total_water, row, col = math.inf, -1, -1
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for row in range(start_row, len(grid)):
            for col in range(0, len(grid[0])):
                if visited[row][col] == 1:
                    continue
                visited[row][col] = 1
                water, r, c = math.inf, -1, -1

                if grid[row][col] == 0:
                    water, r, c = math.inf, -1, -1
                else:
                    water, r, c = find_min_fill(row, col, capacity-1)
                    if water == math.inf:
                        continue

                if total_water == math.inf:
                    total_water = water+1
                    start_row = r
                    start_col = c
                elif total_water > water+1:
                    total_water = water+1
                    start_row = r
                    start_col = c

        return total_water, start_row, start_col

    # find the well with most water
    max_well = -1
    max_well_row, max_well_col = -1, -1

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col
