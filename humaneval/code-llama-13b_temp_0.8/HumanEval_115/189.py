
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
    def flood_fill(start, grid, capacity):
        """
        Given a starting point (x,y), find the number of cells we can fill within
        a given capacity.
        """
        n = len(grid)
        m = len(grid[0])
        queue = [(start[0],start[1],0)]
        # We use the convention that -1 is unknown.
        grid_copy = [x[:] for x in grid]
        grid_copy[start[0]][start[1]] = -1
        count = 0
        while len(queue) > 0:
            x,y,count = queue.pop(0)
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                x_new = x+dx
                y_new = y+dy
                if 0 <= x_new < n and 0 <= y_new < m:
                    if grid_copy[x_new][y_new] == 1 and count + 1 <= capacity:
                        grid_copy[x_new][y_new] = -1
                        queue.append((x_new,y_new,count+1))
        return count

    def search_max(start, grid, capacity):
        """
        Given a starting point (x,y), find the maximum number of cells we can fill
        in a given capacity by exhaustively searching through the entire grid.
        """
        n = len(grid)
        m = len(grid[0])
        # We use the convention that -1 is unknown.
        grid_copy = [x[:] for x in grid]
        grid_copy[start[0]][start[1]] = -1
        max_count = 0
        for x in range(n):
            for y in range(m):
                if grid_copy[x][y] == 1:
                    count = flood_fill((x,y), grid_copy, capacity)
                    max_count = max(max_count, count)
        return max_count

    n = len(grid)
    m = len(grid[0])
    max_
