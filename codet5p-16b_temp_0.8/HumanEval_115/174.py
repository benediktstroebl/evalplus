
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

    R, C = len(grid), len(grid[0])
    def bfs():
        import collections
        queue = collections.deque()
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    while queue:
                        r, c = queue.popleft()
                        grid[r][c] = 0
                        for dr, dc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if 0 <= dr < R and 0 <= dc < C and grid[dr][dc] == 1:
                                grid[dr][dc] = 0
                                queue.append((dr, dc))
        return count

    left, right = 0, math.ceil(C/capacity)
    while left < right:
        mid = left + (right - left) // 2
        if bfs() >= mid:
            right = mid
        else:
            left = mid + 1
    return left
