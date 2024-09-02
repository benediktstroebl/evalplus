
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
    # Best Solution:
    #   Time Complexity: O(R*C)
    #   Space Complexity: O(C)
    def max_fill(grid, bucket_capacity):
        R, C = len(grid), len(grid[0])
        b_left, ans = bucket_capacity, 0

        for row in grid:
            r_sum = sum(row)
            ans += math.ceil(r_sum / bucket_capacity)
            b_left = max(0, b_left - r_sum)
        
        return ans


    # # Naive solution:
    #   Time Complexity: O(R*C)
    #   Space Complexity: O(C)
    # def max_fill(grid, bucket_capacity):
    #     R, C = len(grid), len(grid[0])
    #     b_left, ans = bucket_capacity, 0

    #     for row in grid:
    #         for cell in row:
    #             b_left -= cell
    #             if b_left < 0:
    #                 ans += 1
    #                 b_left = bucket_capacity
        
    #     return ans


    print("Input: grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]")
    print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))

    print("Input: grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]")
    print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))

    print("Input: grid = [[0,0,0], [0,0,0]]")
    print(max_fill([[0,0,0], [0,0,0]], 5))
