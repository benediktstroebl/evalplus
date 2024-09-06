
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

    def num_of_buckets(grid, capacity):
        """
        O(N) Time and O(N) Space
        """
        # def used_capacity(grid, start, end, buckets):
        #     if start > end:
        #         return buckets

        #     if grid[start][end] == 0:
        #         return used_capacity(grid, start+1, end, buckets)
        #     else:
        #         return used_capacity(grid, start+1, end, buckets+1)

        # def used_capacity_optimized(grid, start, end, buckets, capacity):
        #     if start > end:
        #         return buckets

        #     if grid[start][end] == 0:
        #         return used_capacity_optimized(grid, start+1, end, buckets, capacity)
        #     else:
        #         buckets += 1
        #         if buckets > capacity:
        #             return -1
        #         return used_capacity_optimized(grid, start+1, end, buckets, capacity)

        # return used_capacity_optimized(grid, 0, len(grid[0])-1, 0, capacity)
        def used_capacity(grid, start, end, buckets):
            if start > end:
                return buckets

            if grid[start][end] == 0:
                return used_capacity(grid, start+1, end, buckets)
            else:
                buckets += 1
                return used_capacity(grid, start+1, end, buckets)

        def used_capacity_optimized(grid, start, end, buckets, capacity):
            if start > end:
                return buckets

            if grid[start][end] == 0:
                return used_capacity_optimized(grid, start+1, end, buckets, capacity)
            else:
                buckets += 1
                if buckets > capacity:
                    return -1
                return used_capacity_optimized(grid, start+1,
