import math
import collections
def max_fill(grid, capacity):
    wells = collections.Counter(row for row in grid)
    filled_wells = 0
    
    for i, row in wells.items():
        for j, filled in row.items():
            if filled:
                filled_wells += math.ceil(filled / capacity)
                if filled % capacity == 0:
                    continue
                filled_wells += 1  # To lower the bucket an extra time to exactly fill the bucket
    
    return filled_wells