import math
def max_fill(grid, capacity):
    """
    Fills wells in a grid with a certain capacity.
    """
    def fill_well(row):
        total_water = 0
        for j in range(len(row)):
            if row[j] == 1:
                total_water += 1
                if total_water <= capacity:
                    row[j] = 0
                else:
                    row[j] = 1
                    return total_water
        return total_water

    num_buckets = 0
    for i in range(len(grid)):
        num_buckets += fill_well(grid[i])

    return num_buckets
capacity = 1