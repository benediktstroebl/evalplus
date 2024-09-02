
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

    def calc(arr, n, bucket_capacity):
        #init
        capacity = bucket_capacity
        f = 0
        s = 0
        t = 0
        i = 0
        j = 0
        # find max_fill
        while (i < n and j < n):
            while (j < n and arr[i][j] != 1):
                j += 1
            if (j < n):
                while (s < n and t < n and arr[s][t] != 1):
                    t += 1
                if (s < n):
                    if ((t - s) > capacity):
                        capacity = capacity - (t - s)
                        f = f + 1
                        s = s + 1
                    else:
                        capacity = 0
                        s = s + 1
                t = s + 1
            i = i + 1
        return f

    n = len(grid)
    f = calc(grid, n, capacity)
    return f
