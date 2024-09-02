
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
    def find_water_tiles(grid):
        return [i for i in range(len(grid)) if grid[i].count(1) > 0]

    def find_possible_tiles(grid, tiles, capacity):
        possible_tiles = [i for i in tiles if grid[i][0] < capacity]
        for tile in possible_tiles:
            if grid[tile][0] > capacity:
                possible_tiles.remove(tile)
        return possible_tiles

    def find_max_water(grid, tiles, capacity):
        max_water = 0
        for tile in tiles:
            if grid[tile][0] <= capacity:
                max_water = max(max_water, grid[tile][0])
        return max_water

    def empty_water(grid, capacity, tiles):
        water = capacity
        for tile in tiles:
            water -= grid[tile][0]
            grid[tile][0] = 0
        return water

    def fill_water(grid, capacity, tiles):
        for tile in tiles:
            grid[tile][0] += 1
        return

    def fill_additional_water(grid, capacity, tiles):
        water = capacity
        for tile in tiles:
            water -= grid[tile][0]
            grid[tile][0] = capacity

        for tile in tiles:
            grid[tile][0] += water

    def fill_additional_water_optimized(grid, capacity, tiles):
        water = 0
        for tile in tiles:
            water += grid[tile][0]
            grid[tile][0] = capacity
        for tile in tiles:
            grid[tile][0] += water

    tiles = find_water_tiles(grid)
    possible_tiles = find_possible_tiles(grid, tiles, capacity)

    fill_water(grid, capacity, tiles)
    max_water = capacity
    while any(x > 0 for x in grid[0]):
        capacity -= max_water
        tiles = possible_tiles
        possible_tiles = find_possible_tiles(grid, tiles, capacity)
        max_