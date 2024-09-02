
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
    import math
    n = len(grid)
    if n == 0:
        return 0

    m = len(grid[0])
    if m == 0:
        return 0

    bucket_number = n * m
    bucket_amount = capacity
    bucket_capacity = capacity

    def bucket_fills(i, j):
        nonlocal bucket_number, bucket_capacity, bucket_amount, m, n
        if i < 0 or j < 0 or i >= n or j >= m:
            return 0
        if grid[i][j] == 0:
            return 0
        if grid[i][j] is True:
            return 0
        if (i, j) in visited:
            return visited[(i, j)]
        
        visited[(i, j)] = 1
        bucket_amount -= 1
        current_bucket_number = i * m + j
        each_bucket_capacity = bucket_capacity / bucket_number
        current_bucket_capacity = each_bucket_capacity + 1 if bucket_amount % each_bucket_capacity != 0 else each_bucket_capacity
        next_bucket_capacity = each_bucket_capacity - 1
        print(i, j, each_bucket_capacity, current_bucket_capacity, next_bucket_capacity)
        result = bucket_fills(i-1, j) + bucket_fills(i+1, j) + bucket_fills(i, j-1) + bucket_fills(i, j+1)
        visited[(i, j)] -= 1
        return result

    visited = {}

    max_amount = bucket_fills(0, 0)
    return max_amount

assert(max_fill([[1]], 1) == 0)
assert(max_fill([[1,1,1]], 1) == 1)
assert(max_fill([[0,1,0]], 1) == 2)
assert(max_fill([[1,0,0]], 1) == 2)
assert(max_fill([[0,1,1]], 1) == 2)
assert(max_fill([[0,