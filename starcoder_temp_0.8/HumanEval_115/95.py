
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
    # traverse the grid
    # for each row, create a list of buckets
    # 1. for each column that has a 1, put the value into the corresponding bucket
    # 2. for each bucket, if the sum of its contents is larger than capacity, remove the first value and add a new 1
    # 3. add the number of iterations to a list, return the max number of iterations
    # O(M*N) time | O(M) space
    max_number_of_iterations = 0
    for i in range(len(grid)):
        number_of_iterations = 0
        buckets = [0] * len(grid[0])
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                buckets[j] = capacity
        while max(buckets)!= 0:
            number_of_iterations += 1
            for j in range(len(buckets)):
                if buckets[j] == capacity:
                    buckets[j] = 0
                elif buckets[j] > 0:
                    buckets[j] -= 1
        max_number_of_iterations = max(max_number_of_iterations, number_of_iterations)
    return max_number_of_iterations


