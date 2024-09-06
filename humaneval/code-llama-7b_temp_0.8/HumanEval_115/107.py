
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
    # 1st solution: TLE
    # O(nm) time | O(n) space
    # def max_fill(grid, bucket_capacity):
    #     n, m = len(grid), len(grid[0])
    #     result = 0
    #     # print("n = {}, m = {}".format(n, m))
    #     # print(grid)

    #     for i in range(n):
    #         result += int(sum(grid[i]) // bucket_capacity)
    #     # print(result)

    #     # per row
    #     for j in range(m):
    #         result += int(sum(row[j] for row in grid) // bucket_capacity)
    #     # print(result)

    #     # per column
    #     for i in range(n):
    #         for j in range(m):
    #             if grid[i][j] == 1:
    #                 result += int(sum(grid[k][j] for k in range(n)) // bucket_capacity)
    #     # print(result)

    #     # per square
    #     for i in range(n):
    #         for j in range(m):
    #             if grid[i][j] == 1:
    #                 for k in range(i, min(i+bucket_capacity, n)):
    #                     for l in range(j, min(j+bucket_capacity, m)):
    #                         result += 1
    #     # print(result)
    #     return result

    # 2nd solution: TLE
    # O(nm) time | O(n) space
    # def max_fill(grid, bucket_capacity):
    #     n, m = len(grid), len(grid[0])
    #     result = 0
    #     # print("n = {}, m = {}".format(n, m))
    #     # print(grid)

    #     # per row
    #     for j in range(m):
    #         result += int(sum(row[j]
