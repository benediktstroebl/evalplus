
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
    
    grid_h, grid_w = len(grid), len(grid[0])
    print("grid height:", grid_h, "grid width:", grid_w)
    def bfs():
        queue = [(0,0)]
        visited = set()
        while queue:
            (x,y) = queue.pop(0)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= grid_h or ny < 0 or ny >= grid_w:
                    continue
                if (nx,ny) not in visited:
                    if grid[nx][ny] == 0:
                        continue
                    queue.append((nx,ny))
                    if (nx,ny) == (grid_h-1,grid_w-1):
                        return True
        return False

    i, j = 0, 0
    while i < grid_h:
        while j < grid_w:
            value = grid[i][j]
            if value == 0:
                j += 1
                continue
            new_len = math.floor(capacity / value)
            grid[i][j] -= new_len
            if grid[i][j] < 1:
                grid[i][j] = 0
            j += 1
        i += 1
        j = 0
    i, j = 0, 0
    steps = 0
    while i < grid_h:
        while j < grid_w:
            if grid[i][j] == 0:
                j += 1
                continue
            
            if bfs():
                steps += 1
            grid[i][j] += 1
            j += 1
        i += 1
        j = 0

    return steps
