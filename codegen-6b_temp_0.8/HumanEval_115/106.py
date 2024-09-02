
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
    
    def get_costs(grid):
        wells = grid.shape[1]
        costs = [[0 for j in range(wells)] for i in range(wells)]
        
        for i in range(wells):
            for j in range(wells):
                if grid[i][j] == 1:
                    for k in range(wells):
                        if k != i and grid[k][j]:
                            costs[i][j] += math.ceil(float(grid[k][j]) / 2.0)
                            grid[k][j] -= math.ceil(float(grid[k][j]) / 2.0)
        return costs
    
    def min_fill_costs(grid, costs):
        wells = grid.shape[1]
        min_costs = [[0 for j in range(wells)] for i in range(wells)]
        
        for i in range(wells):
            for j in range(wells):
                if grid[i][j] == 1:
                    for k in range(wells):
                        if k != i and grid[k][j]:
                            min_costs[i][j] += min(min_costs[i][j - 1], min_costs[i - 1][j - 1], min_costs[i - 1][j]) + costs[k][j]
                            grid[k][j] -= min(min_costs[i][j - 1], min_costs[i - 1][j - 1], min_costs[i - 1][j])
        
        return min_costs
    
    def get_max_fill_amount(min_costs):
        wells = min_costs.shape[1]
        
        if wells == 1:
            return 0
        
        max_fill_amounts = [[0 for j in range(wells)] for i in range(wells)]
        
        for i in range(wells):
            for j in range(wells):
                if i == wells - 1 and j == wells - 1:
                    max_fill_amounts[i][j] = min_costs[well