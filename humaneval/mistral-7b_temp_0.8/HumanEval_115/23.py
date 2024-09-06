
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

    if not grid:
        return 0

    # note: i.e. capacity is a parameter, so the grid size is independent of the capacity,
    # thus there is no need to set the capacity as the grid's size.
    m = len(grid)
    n = len(grid[0])

    def fill(grid, bucket_capacity):
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        dist = [[math.inf for j in range(n)] for i in range(m)]
        dist[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1])
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j])

        #
