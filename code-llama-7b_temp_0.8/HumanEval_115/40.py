
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
    # The problem can be divided into two steps:
    # 1. Go through each row and add the units of water in each column to an array.
    # 2. Go through the units array and extract the water with the bucket until the array is empty.

    # Function to add the units of water in each column to an array
    def add_water(grid, water_array):
        # Start at the last column and traverse the columns in reverse order
        for col in range(len(grid[0]) - 1, -1, -1):
            # If the column is not empty, add the units of water to the array
            if grid[0][col] != 0:
                water_array.append(grid[0][col])

    # Function to extract the water with the bucket until the array is empty
    def extract_water(bucket_capacity, water_array):
        count = 0
        # While there are units of water in the array
        while water_array:
            # If the bucket capacity is less than the units of water in the array
            if bucket_capacity < len(water_array):
                # Extract the units of water to the bucket
                bucket_capacity += water_array[0]
                # Remove the units of water from the array
                water_array.remove(water_array[0])
            else:
                # Extract all the units of water in the array to the bucket
                bucket_capacity += sum(water_array)
                water_array.clear()
            count += 1
        return count

    # Initialize the variables
    count = 0
    water_array = []

    # Go through each row and add the units of water in each column to the array
    for row in grid:
        add_water(row, water_array)

    # Go through the units array and extract the water with the bucket
    count += extract_water(capacity, water_array)

    # Output the number of times you need to lower the buckets
    return count

