
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

    def fill(grid, capacity, i, j):
        """
        Fills the bucket by filling up as many cells as possible.
        The bucket is full after i + j == capacity
        """
        if i + j == capacity:
            return 1
        return 2 + fill(grid, capacity, i + 1, j + 1)

    def backtrack(grid, capacity, i, j):
        """
        Goes through all possible combinations of i and j.
        """
        if i == capacity:
            return 1
        if i + j > capacity:
            return 0
        return backtrack(grid, capacity, i + 1, j) + backtrack(grid, capacity, i, j + 1)

    def get_all_combinations(capacity, i, j):
        """
        Takes all possible combinations of i and j,
        and passes them on to backtrack.
        """
        for i in range(1, capacity):
            for j in range(1, capacity):
                if i + j == capacity:
                    continue
