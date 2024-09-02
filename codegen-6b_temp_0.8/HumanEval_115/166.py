
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
    rows = len(grid)
    cols = len(grid[0])
    
    # Mark the source wells as not visited
    sources = []
    visited = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                visited[r][c] = 1
                sources.append((r, c, 0))

    count = 0
    while len(sources) > 0:
        r, c, count = sources.pop()
        for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= rr < rows and 0 <= cc < cols and visited[rr][cc] == 0 and grid[rr][cc] == 0:
                visited[rr][cc] = 1
                sources.append((rr, cc, count + 1))
                grid[rr][cc] = 1
                if count + 1 >= capacity:
                    return count + 1
    
    return count
