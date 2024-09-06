import math
def max_fill(grid, capacity):
    """
    Use buckets to empty wells of water. Return num times buckets lowered.
    """
    # Create a 2D counter for wells
    dfc = {}
    for i in range(len(grid)):
        dfc[i] = {}
        for j in range(len(grid[i])):
            dfc[i][j] = 0 if grid[i][j] == '0' else dfc[i][j] + 1 + dfc[i][j-1] + dfc[i-1][j] + dfc[i-1][j-1]

    # Create a list to store maximum fillings
    max_fillings = []
    
    # Consider all capacities from 1 to the size of the grid
    for b in range(1, capacity + 1):
        # Create a 2D counter for filled water
        filled = {}
        for i in range(len(grid)):
            filled[i] = {}
            for j in range(len(grid[i])):
                if dfc[i][j] >= b:
                    filled[i][j] = dfc[i][j] - b
                    filled[i][j-1] = dfc[i][j-1] - b
                    filled[i-1][j] = dfc[i-1][j] - b
                    filled[i-1][j-1] = dfc[i-1][j-1] - b
        
        # Initialize maximum filling for current capacity
        max_fill_curr = 0
        
        # Consider all wells
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # Update max filling if a well can be emptied
                if filled[i][j] + filled[i][j-1] + filled[i-1][j] + filled[i-1][j-1] >= b:
                    max_fill_curr = max(max_fill_curr, filled[i][j] + filled[i][j-1] + filled[i-1][j] + filled[i-1][j-1])
                    
        max_fillings.append(max_fill_curr)
        
    return max(max_fillings)