
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

    # Extract wells data
    wells_data = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                wells_data.append((i,j))
    
    # Extract wells x and y coordinates
    wells_coordinates = []
    for i in range(len(wells_data)):
        wells_coordinates.append((wells_data[i][0], wells_data[i][1]))

    # Sort wells
    wells_coordinates.sort(key=lambda x: x[1])

    # Extract number of wells
    n_wells = len(wells_data)

    # Init number of times to empty the buckets
    times_to_empty_buckets = 0

    # Init first coordinates
    first_coordinate = wells_coordinates[0]

    # Init last coordinates
    last_coordinate = wells_coordinates[n_wells-1]

    # Init first and last row
    first_row = last_row = first_coordinate[0]

    # While we haven't find the bottom of the wells
    while last_row <= first_row:
        # Init left most well
        left_most_well = 0

        # Init right most well
        right_most_well = n_wells - 1

        # Init wells to fill
        wells_to_fill = []

        # While we haven't find the top of the wells
        while left_most_well <= right_most_well:
            # Get current well coordinate
            current_well = wells_coordinates[left_most_well]

            # If current well is the first row
            if current_well[0] == first_row:
                # Add well to wells to fill
                wells_to_fill.append(current_well)

                # Increment left most well
                left_most_well += 1

            # Else, current well is not the first row
            else:
                # Decre
