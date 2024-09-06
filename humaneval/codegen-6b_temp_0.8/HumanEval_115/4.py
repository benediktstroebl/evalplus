
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
    n2 = len(grid[0])
    arr = [[0 for _ in range(0, n2)] for _ in range(0, n)]
    for i in range(0, n):
        for j in range(0, n2):
            if grid[i][j] == 1:
                arr[i][j] = 1
    #
    # def count_holes(grid, start, end, capacity):
    #     import math
    #     result = 0
    #     if grid[start][end] != 1:
    #         return result
    #     queue = [((start, end), capacity)]
    #     while queue:
    #         (a, b), n = queue.pop(0)
    #         result += n
    #         if a == start:
    #             if b == end:
    #                 result -= 1
    #             else:
    #                 queue.append(((a, b + 1), n))
    #         elif b == end:
    #             queue.append(((a + 1, b), n))
    #         else:
    #             queue.append(((a + 1, b), n))
    #             queue.append(((a, b + 1), n))
    #     return result
    #
    # result = 0
    #
    # for i in range(0, n):
    #     result += count_holes(grid, i, 0, bucket_capacity)
    #     result += count_holes(grid, i, n2 - 1, bucket_capacity)
    #
    # for j in range(0, n2):
    #     result += count_holes(grid, 0, j, bucket_capacity)
    #     result += count_holes(grid, n - 1, j, bucket_capacity)
    #
    # return result

    def find_max_height(grid, i, j, capacity, height):
        height_max = height
        if grid[i][j] != 1:
            return height_max
        queue = [(i, j)]
        while queue:
            grid[queue[0][0]][queue[0][