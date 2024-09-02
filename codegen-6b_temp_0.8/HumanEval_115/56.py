
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
    m = len(grid[0])

    import math

    def calculate_area(i, j):
        return (i + 1) * (j + 1)

    def show_area(i, j):
        return ' ' * (n - i - 1) + '#' * (j + 1) + '\n'
    
    def grid_row_sum(i):
        return sum(grid[i])

    def count_buckets():
        import math
        return int(math.log(capacity, 2))

    from collections import defaultdict

    # start: (row, _)
    # end: (row, column)
    # l: column
    # m: row

    # print_grid(grid)

    start = (0, 0)
    end = (n - 1, m - 1)
    l = m - 1
    m = n - 1
    # print(start, end, l, m)

    # print_grid(grid)

    buckets = defaultdict(int)
    bucket_count = count_buckets()

    for x in range(l):
        # print_grid(grid)
        # print_grid(grid, True)

        # print(x, x + 1, x + 2, x + 3, x + 4)
        # print_grid(grid)

        # print(grid_row_sum(x), buckets[x], sum(grid[x]))

        if grid_row_sum(x) == capacity:
            if grid_row_sum(x + 1) > 0:
                buckets[x + 1] += 1
        else:
            buckets[x] = 0

        if grid_row_sum(x + 1) == capacity:
            if grid_row_sum(x + 2) > 0:
                buckets[x + 2] += 1
        else:
            buckets[x + 1] = 0

        if grid_row_sum(x + 2) == capacity:
            if grid_row_sum(x + 3) > 0:
                buckets[x + 3] += 1
        else:
            buckets[x + 2