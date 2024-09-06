import math
def max_fill(grid, capacity):
    wells, height = len(grid), len(grid[0])
    if not wells or not height:
        return 0

    max_level = 0
    start_level = 0
    
    # Calculate the maximum level of water in the wells
    for i in range(wells):
        current_level = 0
        for j in range(height):
            if grid[i][j] == 1:
                current_level += 1
            else:
                max_level = max(max_level, current_level)
                current_level = 0
        
        max_level = max(max_level, current_level)
        start_level += current_level
    
    # Calculate the number of trips needed to empty the wells
    trips = math.ceil(max_level / capacity)
    
    # Calculate the number of trips starting from the first row
    return max(trips - start_level // capacity, 0)