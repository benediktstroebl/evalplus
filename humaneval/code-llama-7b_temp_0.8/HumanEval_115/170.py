
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
    n = len(grid)
    m = len(grid[0])
    capacity = bucket_capacity
    count = 0
    #print(n,m)
    #print(grid)
    for i in range(n):
        cur = grid[i]
        for j in range(len(cur)):
            if cur[j] == 0:
                continue
            else:
                for k in range(i + 1, n):
                    if grid[k][j] != 0:
                        count += 1
                        grid[k][j] += cur[j]
                        if grid[k][j] > capacity:
                            count += math.ceil(grid[k][j] / capacity) - 1
                        grid[k][j] = grid[k][j] % capacity
                        break
    return count

