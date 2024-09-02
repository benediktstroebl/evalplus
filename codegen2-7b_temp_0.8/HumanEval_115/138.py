
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
    def fill_buckets(grid, capacity):
        import collections
        que = collections.deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    que.append((i, j))
                while que:
                    cur_pos = que.popleft()
                    if cur_pos == (i, j):
                        count += 1
                        if len(que) == 0:
                            break
                        for pos in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                            if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == 1:
                                que.append(pos)
        return
