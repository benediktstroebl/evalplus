
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
    row,col=grid.shape
    row_capacity=[[0]*col for _ in range(row)]
    for i in range(row):
        row_capacity[i][0]=capacity
        for j in range(1,col):
            if grid[i][j]=1:
                row_capacity[i][j]=max(row_capacity[i][j],row_capacity[i][j-1]+1)
    min_times=math.ceil(math.log2(len(grid)))
    for i in range(1,min_times):
        for j in range(col):
            if row_capacity[i][j]>0:
                row_capacity[i][j]=0
                for k in range(i-1,min_times+1):
                    for k_j in range(col):
                        if row_capacity[k][k_j]>0:
                            row_capacity[k][k_j]=0
    return min_times