
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
    import math
    rows, cols = len(grid), len(grid[0])
    hori_start = [0] * cols
    vert_start = [0] * cols
    hori_end = [0] * cols
    vert_end = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                hori_start[j] = max(hori_start[j], i)
                vert_start[i] = max(vert_start[i], j)
                hori_end[j] = i
                vert_end[i] = j

    # print(hori_start, vert_start)
    # print(hori_end, vert_end)

    ans = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                ans += 1
                continue
            cur_end = min(hori_end[j], vert_end[i])
            if cur_end == 0:
                ans += 1
                continue
            # print(hori_start[j], hori_end[j], vert_start[i], vert_end[i])
            ans += max(hori_end[j] - hori_start[j], vert_end[i] - vert_start[i])
    return ans

