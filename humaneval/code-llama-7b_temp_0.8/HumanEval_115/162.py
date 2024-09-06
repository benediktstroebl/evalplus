
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
    if grid == [] or grid[0] == []:
        return 0
    n = len(grid)
    m = len(grid[0])
    # print(n,m)
    p = capacity
    # print(p)
    ans = 0
    cur = 0
    while cur < m:
        cur_sum = sum([grid[i][cur] for i in range(n)])
        cur_ans = 0
        while cur_sum < p:
            cur_ans += 1
            next_sum = sum([grid[i][cur+1] for i in range(n)])
            if next_sum < cur_sum:
                return -1
            cur_sum = next_sum
            cur += 1
        if cur_ans != 0:
            ans += cur_ans
            cur += 1
        # print(cur_ans)
        # print(cur)
    # print(ans)
    return ans
