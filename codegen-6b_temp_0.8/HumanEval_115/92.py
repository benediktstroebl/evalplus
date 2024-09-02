
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

    def bfs(r, c):
        q = deque([(r, c)])
        # Set visited to False instead of True
        visited[r][c] = False
        level = 0
        while q:
            for _ in range(len(q)):
                rn, cn = q.popleft()
                for nrn, ncn in [(rn - 1, cn), (rn + 1, cn), (rn, cn - 1), (rn, cn + 1)]:
                    if 0 <= nrn < R and 0 <= ncn < C:
                        if visited[nrn][ncn] and grid[rn][cn] <= grid[nrn][ncn]:
                            visited[nrn][ncn] = False
                            q.append((nrn, ncn))
            level += 1
            
        return level
    
    R, C = len(grid), len(grid[0])
    
    result = 0
    for r in range(R):
        for c in range(C):
            visited = [[False] * C for i in range(R)]
            level = bfs(r, c)
            if level > 0:
                result += level - 1
                # Set the grid to '0'
                grid[r][c] = 0
    return result

