
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
    
    # 1st try: O(N^2)
    # rows, cols = len(grid), len(grid[0])
    # cnt = 0
    # for r in range(rows):
    #     for c in range(cols):
    #         if grid[r][c] == 1:
    #             for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #                 nr, nc = r+dr, c+dc
    #                 if 0 <= nr < rows and 0 <= nc < cols:
    #                     if grid[nr][nc] == 0:
    #                         cnt += 1
    #                         grid[nr][nc] = 1
    #                         break
    # return cnt

    # 2nd try: O(N)
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                n = int(math.ceil(capacity/float(grid[r][c])))
                while n >= 1 and r+n < rows and c+n < cols:
                    grid[r+n][c+n] -= n
                    n -= 1
                cnt += n
                grid[r][c] = 0
    return cnt
