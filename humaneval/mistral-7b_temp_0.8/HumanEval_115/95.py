
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
    # 3 ways to solve this problem
    # 1. Use brute force approach to get all the possible combinations
    # 2. Use dynamic programming approach to optimize the solution
    # 3. Use greedy approach to get the solution

    # ///////////////////////////////////////////////////////////////////////////////////

    # BRUTE FORCE APPROACH
    def brute_force(grid, capacity):
        result = 0
        while True:
            if sum(sum(i) for i in grid) <= capacity:
                return result
            if grid[0][0] == 0:
                result += 1
                break
            i = 0
            while i < len(grid):
                j = 0
                while j < len(grid[0]):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                        j += capacity
                    else:
                        j += 1
                i += 1
        return result

    # ///////////////////////////////////////////////////////////////////////////////////

    # DYNAMIC PRO
