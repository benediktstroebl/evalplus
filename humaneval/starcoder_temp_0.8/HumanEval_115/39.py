
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
    count = 0

    while True:
        current_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for n, (nr, nc) in enumerate([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]):
                        if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            current_count += 1
        if not current_count:
            break
        count += math.ceil(current_count / capacity)

    return count

