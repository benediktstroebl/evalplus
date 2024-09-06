
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
    # i, j = 0, 0
    # c = capacity
    # if c == 0:
    #     return 0
    # count = 0
    # while c > 0:
    #     if grid[i][j] == 0:
    #         break
    #     grid[i][j] = 0
    #     c -= 1
    #     count += 1
    #     if i == j and i == len(grid)-1:
    #         j = i - 1
    #     elif i == j and i < len(grid)-1:
    #         j += 1
    #     elif i < len(grid)-1 and i < j:
    #         j = 0
    #         i += 1
    #     else:
    #         j -= 1
    #     if j == len(grid)-1 and c == 0:
    #         break
    #     if c == 0 and grid[i][j] == 0:
    #         grid[i][j] = 1
    #         c += 1
    #         count += 1
    # return count

    from collections import deque
    count = 0
    for i in range(len(grid)):
        q = deque()
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and len(q) == capacity:
                q.popleft()
                count += 1
            elif grid[i][j] == 1:
                q.append(1)
    return count
