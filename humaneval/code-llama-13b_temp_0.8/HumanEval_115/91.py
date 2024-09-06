
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
    # to solve this we need to check the patterns
    # wells with no water at all can be skipped
    # wells with at most the capacity water can be filled completely
    # wells with more than the capacity can be filled partially and the remaining amount can be extracted
    #                                                               from other wells
    # all combinations of filling/extracting from wells with partial water
    #                                                               have to be checked to see which combination
    #                                                               results in the least filling
    # we can generate the combinations with a bfs algorithm
    # we need to keep track of the total water in each well, the total water in each row,
    #                                                            and the max water that can be extracted from a well
    #                                                            in the current configuration
    # we start with the configuration where we fill the first well in each row
    # we store the configuration as a tuple (water in each well, total water in each row, max water that can be extracted)
    # we check if we can fill/extract more water from a well
    #                                   if not, we can move on to the next configuration
    # after we've found the lowest configuration we can extract the total number of steps
    #
    # time complexity:  O(n^2)
    # space complexity: O(n)
    # """
    # Input: 
    #     grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    #     bucket_capacity : 2
    # Output: 5
    # """
    # print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
    # print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 3))
    # print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0
