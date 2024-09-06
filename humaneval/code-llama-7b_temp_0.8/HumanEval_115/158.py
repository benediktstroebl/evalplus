
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
    def calculate_max_water(grid, buckets, capacity):
        # Scan the grid from top to bottom to calculate the maximum amount of water that can be extracted
        # from each well.
        max_water = 0
        buckets = buckets.copy()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    buckets[j] += 1
                else:
                    buckets[j] = 0
                # print(f"{i},{j}: {buckets[j]}")
            max_water += min(buckets)
            # print(f"{i}: {max_water}\n{buckets}")
        return max_water

    def lower_buckets(grid, buckets, capacity, amount):
        """
        You need to lower the buckets in a way to maximize the amount of water
        extracted from the wells.
        Each bucket needs to be lowered by a single unit.
        """
        # Find the maximum amount of water in the grid.
        max_water = amount
        # print(f"max_water: {max_water}")
        # print(f"max_water - buckets: {max_water - buckets}")
        while max_water - buckets > capacity:
            # Find the minimum amount of buckets in the grid.
            min_buckets = math.inf
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        buckets[j] += 1
                    else:
                        buckets[j] = 0
                    min_buckets = min(min_buckets, buckets[j])
                    # print(f"{i},{j}: {buckets[j]}")
            # print(f"min_buckets: {min_buckets}")
            if min_buckets == math.inf:
                return amount
            # Each bucket needs to be lowered by 1.
            amount -= min_buckets
            max_water
