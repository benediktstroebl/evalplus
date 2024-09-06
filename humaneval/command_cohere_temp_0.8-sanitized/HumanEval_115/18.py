import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    buckets = len(grid)

    def fill_level(row):
        return sum(row)

    water_level = [fill_level(row) for row in grid]
    water_level = [math.ceil(water / capacity) for water in water_level]
    return max(water_level) * buckets