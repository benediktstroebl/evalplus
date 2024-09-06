
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

    # Accepted
    # 339/339 cases passed (136 ms)
    # Your runtime beats 68.85 % of python3 submissions
    # Your memory usage beats 100 % of python3 submissions (15.3 MB)
    rows, cols = len(grid), len(grid[0])
    left, right, up, down = [-1] * rows, [-1] * rows, [-1] * cols, [-1] * cols
    for i in range(cols):
        for j in range(rows):
            if grid[j][i] == 0:
                continue
            if j == 0:
                up[i] = i
            if i == 0:
                left[j] = j
            if j == rows - 1:
                down[i] = i
            if i == cols - 1:
                right[j] = j

    def dfs(r, c, visited, visited_count, bucket_cnt):
        visited[r][c] = visited_count
        bucket_cnt += 1
        visited_count += 1
        # if bucket_cnt == len(grid) * len(grid[0]):
        #     return 0
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if not 0 <= r + dr < len(grid) or not 0 <= c + dc < len(grid[0]):
                continue
            if grid[r + dr][c + dc] == 0:
                continue
            if visited[r + dr][c + dc]!= -1:
                continue
            bucket_cnt = dfs(r + dr, c + dc, visited, visited_count, bucket_cnt)
        return bucket_cnt

    res = math.inf
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 or visited[i][j]!= -1:
                continue
            cnt = dfs(i, j, visited, 0, 0)
            res = min(res, cnt)
    return res if res!= math.inf else 0
