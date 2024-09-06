
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

    # TODO: bad algo!

    # grid
    # rows
    # columns

    def _lower_buckets(row, bucket_capacity):
        """
        this is O(n)
        """
        # 1. iterate over the row
        # 2. if the current well > bucket_capacity
        #    then:
        #        a. if there is no well in the next row
        #           then:
        #               i. lower the bucket
        #               ii. continue to the next well in the row
        #           else:
        #               i. extract water from the current well
        #               ii. go to the next well in the row
        #        else:
        #           extract water from the current well

        num_of_buckets = 0
        water_extracted = 0
        last_index = len(row) - 1
        for i in range(len(row)):
            current_well = row[i]
            water_extracted += current_well
            if water_extracted > bucket_capacity:
                if i == last_index:
                    num_of_buckets += 1
                    water_extracted = 0
                else:
                    next_well = row[i + 1]
                    water_extracted -= next_well
                    if water_extracted > bucket_capacity:
                        num_of_buckets += 1
                        water_extracted = 0

        return num_of_buckets

    def _max_fill(grid, capacity):
        """
        find the max value
        """
        max_value = 0
        for row in grid:
            current_value = _lower_buckets(row, capacity)
            if current_value > max_value:
                max_value = current_value
        return max_value

    return _max_fill(grid, capacity)

