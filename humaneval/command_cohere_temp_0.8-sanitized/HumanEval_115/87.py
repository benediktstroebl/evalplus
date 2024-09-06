import math
def max_fill(grid, capacity):
    wells, w = len(grid), len(grid[0])
    fill_count = [0] * wells
    max_fill_count = 0

    for i in range(wells):
        water_count = 0
        for j in range(w):
            if grid[i][j] == 1:
                water_count += 1
                if water_count <= capacity:
                    fill_count[i] = water_count
                else:
                    fill_count[i] = capacity
                    max_fill_count += 1
                    water_count -= capacity
        if water_count > 0:
            max_fill_count += water_count

    return max_fill_count