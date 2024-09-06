
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

    def extract_water_from_wells(grid, capacity):
        """
            This function tries to extract all the available water from each well
            and to store it in a bucket.
            The function returns the number of times that it has been used to 
            extract water from each well.

            The algorithm runs from top to bottom.
            If there are more than one unit of water, then it will try to extract 
            as many units as it can from the highest well.
            If there is only a single unit of water in the well, 
            then it will try to extract one unit of water.
            It will continue until the well is empty.
        """
        wells = []
        for i in range(len(grid)):
            row_list = []
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    row_list.append(j)
            wells.append(row_list)

        buckets = []
        wells_used = 0
        for i in range(len(wells)):
            if wells[i]:
                buckets.append([])
                bucket = buckets[-1]
                while len(wells[i]) > 0:
                    well = wells[i].pop(0)
                    well_filled = min(capacity, grid[i][well])
                    bucket.append(well_filled)
                    grid[i][well] -= well_filled
                    wells_used += 1

                well_index = i
                while wells[well_index]:
                    well = wells[well_index].pop(0)
                    well_filled = min(capacity, grid[well_index][well])
                    bucket = buckets[well_index]
                    bucket.append(well_filled)
                    grid[well_index][well] -= well_filled
                    wells_used += 1
                    well_index += 1
                    if well_index >= len(wells):
                        well_index = 0

        return wells_used

    def max_fill_of_wells
