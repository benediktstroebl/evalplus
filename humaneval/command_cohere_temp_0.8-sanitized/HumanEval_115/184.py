import numpy as np
def max_fill(grid, capacity):
    # Create a numpy array from the grid
    well_array = np.array(grid)
    
    # Calculate the total water in each well
    total_water = np.sum(well_array, axis=1)
    
    # Calculate the maximum water that can be held in a single bucket
    max_water = np.max(total_water)
    
    # Calculate the number of trips needed to empty all wells
    trips = np.ceil(total_water / max_water)
    
    return trips.sum()