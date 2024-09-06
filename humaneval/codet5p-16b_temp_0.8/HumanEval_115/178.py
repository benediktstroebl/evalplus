
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

    def get_buckets_needed(grid):
        grid = [[1 if cell == 1 else 0 for cell in row] for row in grid]
        count = 0
        for row in grid:
            for i in range(len(row)):
                if row[i] == 1:
                    count += 1
                    for j in range(i, len(row)):
                        row[j] = 0
        return count

    def water_fill(grid, capacity):
        max_count = 0
        for row in grid:
            for i in range(len(row)):
                if row[i] == 1:
                    max_count += 1
                    for j in range(i, len(row)):
                        row[j] = 0
        return math.ceil(max_count / capacity)

    return water_fill(grid, capacity) - get_buckets_needed(grid)
