
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

    bucket_capacity = capacity
    m = len(grid)
    n = len(grid[0])
    start = [0, 0]
    end = [m-1, n-1]
    cells = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                cells.append([i,j])

    def get_total_water(grid, bucket_capacity, start, end, cells):
        import math
        total_water = 0
        total_cells = len(cells)
        for cell in cells:
            cell_water = math.floor(bucket_capacity * grid[cell[0]][cell[1]])
            total_water += cell_water
            for i in range(cell[0], start[0]):
                if grid[i][cell[1]] == 1:
                    grid[i][cell[1]] -= cell_water / (end[0] - start[0])
                else:
                    grid[i][cell[1]] += cell_water / (end[0]
