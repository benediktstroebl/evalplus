
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

    INF = 10 ** 9
    size_row, size_col = len(grid), len(grid[0])

    left_to_right = [[0] * size_col for _ in range(size_row)]
    up_to_down = [[0] * size_col for _ in range(size_row)]

    # initialization
    for i in range(size_row):
        for j in range(size_col):
            if grid[i][j] == 1:
                left_to_right[i][j] = INF
                up_to_down[i][j] = INF
            else:
                if j > 0:
                    left_to_right[i][j] = left_to_right[i][j - 1]
                if i > 0:
                    up_to_down[i][j] = up_to_down[i - 1][j]

    for i in range(size_row - 2, -1, -1):
        for j in range(size_col - 1, -1, -1):
            if j < size_col - 1:
                left_to_right[i][j] = min(
                    left_to_right[i][j], left_to_right[i][j + 1] + 1
                )
            if i < size_row - 1:
                up_to_down[i][j] = min(up_to_down[i][j], up_to_down[i + 1][j] + 1)

    answer = 0
    for i in range(size_row):
        for j in range(size_col):
            if grid[i][j] == 1:
                answer += min(
                    math.ceil((size_row - i) / (size_row - 1)),
                    math.ceil((size_col - j) / (size_col - 1)),
                    math.ceil(
                        left_to_right[i][j] * (size_col - j) / (size_col - 1)
                    ),
                    math.ceil(
                        up_to_down[i][j] * (size_row - i) / (size_row - 1)
                    ),
                )

    return answer

