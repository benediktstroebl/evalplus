
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
    from collections import deque
    def bfs(grid, capacity):
        visited = set()
        q = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    visited.add((row, col))
                    q.append((row, col))
        
        #print(visited)
        #print(q)
        water_level = capacity
        level_history = {}
        level_history['water_level'] = water_level
        level_history['time'] = 0
        level_history['visited'] = visited
        level_history['seen'] = {(row, col): 1 for row in range(len(grid)) for col in range(len(grid[0]))}
        level_history['q'] = q

        while len(q) > 0:
            row, col = q.popleft()
            water_level -= 1
            level_history['water_level'] = water_level
            level_history['seen'][(row, col)] = 0
            #print(q, row, col)
            if (row, col) in level_history['visited']:
                #print('outside', level_history, row, col)
                continue

            if (row, col) in level_history['seen']:
                continue

            level_history['q'].append((row, col))
            level_history['seen'][(row, col)] = 1
            level_history['time'] += 1
            
            if water_level == 0:
                #print('water_level')
                level_history['seen'][(row, col)] = 0
                water_level += 1
                level_history['water_level'] = water_level
                level_history['time'] += 1
                #print(level_history)
                continue

            neighbors = neighbor_coords(row, col, grid)
            for n_row, n_col in neighbors:
                if (n_row, n_col) in level_history['visited']:
                    continue
                if grid[n_row][n