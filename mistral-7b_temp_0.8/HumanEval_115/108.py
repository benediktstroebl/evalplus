
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
    # 这个思路是不对的，这个思路是基于二分法，但是题目要求是最小次数，所以这个是最大次数
    # 也就是说，要遍历每个位置的最大值，然后遍历每个位置的最小值
    # 这两个最小值是最大次数
    # 我们有最大次数，最小次数，那么就得到了最后的答案

    # 先遍历一遍，计算每个位置的最大值，然后遍历一遍计算每个位置的最小值
    # 因为我们要使用二分法，所以我们需要知道是最大次数还是最小次数
    # 如果是最大次数，那么需要遍历一遍计算每个位置的最大值，然后再遍历一遍计算每个位置的最小值
    # 如果是最小次数，那么需要
