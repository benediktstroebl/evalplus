
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
    # 1) return the min number of times to empty the wells, given that you can only use one bucket
    # 2) return the min number of times to empty the wells, given that you can use multiple buckets of any size
    # 3) return the min number of times to empty the wells, given that you can use multiple buckets of the same size
    # 4) return the min number of times to empty the wells, given that you can use multiple buckets of the same size,
    #    and that you can use the buckets in any order

    # https://leetcode.com/problems/maximum-units-on-a-truck/
    def numOfUnits(grid, bucket):
        def numOfBuckets(n):
            return math.ceil(n/bucket)

        # fill each well in grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = numOfBuckets(grid
