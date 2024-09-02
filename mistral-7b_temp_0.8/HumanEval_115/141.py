
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
    def max_fill(grid, capacity):
        import math
        n = len(grid)
        visited = set()
        queue = []
        cur_max_fill = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
        while queue:
            row, col = queue.pop(0)
            for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                r = row + dr
                c = col + dc
                if 0 <= r < n and 0 <= c < n and (r,c) not in visited:
                    if grid[r][c] == 1:
                        if capacity - 1 <= cur_max_fill:
                            cur_max_fill = math.inf
                        else:
                            cur_max_fill += 1
                        visited.
