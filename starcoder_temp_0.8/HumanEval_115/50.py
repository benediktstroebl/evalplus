
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
    # Approach 1: Brute force
    # O(n) time | O(n) space
    def get_coords(grid):
        # List all coordinates in grid where there is a 1
        coords = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    coords.append((i, j))
        return coords

    def find_max_volume_well(coords, capacity):
        # Find the well with maximum volume in the list of coords
        max_volume = 0
        for coord in coords:
            max_volume = max(max_volume, get_volume(coord, capacity))
        return max_volume

    def get_volume(coord, capacity):
        # Get the volume of water in the well with given coord
        (i, j) = coord
        volume = 0
        # Search all 8 directions in a 2D grid
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                # Don't count out-of-bounds wells or wells with 0 capacity
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] and grid[x][y] <= capacity:
                    volume += grid[x][y]
        return volume

    # Get the list of coordinates where there is a 1
    coords = get_coords(grid)
    # Find the max volume well in the list of coords
    max_volume_well = find_max_volume_well(coords, capacity)
    # If the max volume well's volume > capacity, we need to lower the bucket
    return math.ceil(max_volume_well / capacity)
