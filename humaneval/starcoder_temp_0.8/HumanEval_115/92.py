
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
    # Your code here
    # import numpy as np
    # buckets = np.zeros(grid.shape)
    # buckets[grid == 1] = capacity
    # n, m = buckets.shape
    # print(buckets)
    # print(n, m)
    # empty = []
    # for i in range(n):
    #     for j in range(m):
    #         if buckets[i, j] == 0:
    #             continue
    #         elif buckets[i, j] == capacity:
    #             return -1
    #         elif i == 0:
    #             empty.append((i, j))
    #             continue
    #         else:
    #             for ii in range(i-1, -1, -1):
    #                 if buckets[ii, j]!= capacity:
    #                     continue
    #                 else:
    #                     continue
    #     if len(empty) == 0:
    #         return -1
    #     else:
    #         i, j = empty.pop()
    #         for k in range(j+1, m):
    #             if buckets[i, k]!= 0:
    #                 continue
    #             else:
    #                 buckets[i, k] = capacity
    #                 break
    #         for k in range(i-1, -1, -1):
    #             if buckets[k, j]!= 0:
    #                 continue
    #             else:
    #                 buckets[k, j] = capacity
    #                 break

    # for i in range(n-1, -1, -1):
    #     for j in range(m-1, -1, -1):
    #         if buckets[i, j]!= capacity:
    #             continue
    #         else:
    #             for k in range(j-1, -1, -1):
    #                 if buckets[i, k]!= capacity:
    #                     continue
    #                 else:
    #                     buckets[i, k] = capacity
    #                     break
    #             for k in range(i-1, -1, -1):
    #                 if buckets[k, j]!= capacity:
    #                     continue
    #                 else:
    #                     buckets[k, j] = capacity
    #                     break
    # if buckets.any():
    #     return -
