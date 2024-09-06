
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

    def bfs(grid, capacity):
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        queue = [(0, 0, 0)]
        while queue:
            row, col, water = queue.pop(0)
            if visited[row][col] == 1:
                continue
            visited[row][col] = 1
            if grid[row][col] == 1:
                water += 1
                if water > capacity:
                    return math.ceil((water - capacity)/capacity)
            if row > 0 and visited[row-1][col] == 0:
                queue.append((row-1, col, water))
            if row < ROWS-1 and visited[row+1][col] == 0:
                queue.append((row+1, col, water))
            if col > 0 and visited[row][col-1] == 0:
                queue.append((row, col-1, water))
            if col < COLS-1 and visited[row
