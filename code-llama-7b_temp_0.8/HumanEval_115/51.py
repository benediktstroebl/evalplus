
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

    def extract_water(row):
        """
        Extract water from a row and return how much water we could extract.

        Examples:
            grid: [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            row_idx: 0

            Output: 1 (we could extract 1 unit of water)

            grid: [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            row_idx: 1

            Output: 2 (we could extract 1 unit of water + 1 unit of water)
        """
        # Find the index of the leftmost 1 in the row
        # Go backwards in the row
        # Empty buckets while their capacity is less than the difference between the last 1 and the current index
        # Note that in both cases the last 1 should be in the leftmost 1
        import math
        row_idx = row.index(1)

        extracted_water = 0
        for i in range(len(row)-1, row_idx-1, -1):
            if capacity >= (i-row_idx+1):
                extracted_water += i-row_idx+1
                capacity -= i-row_idx+1
            else:
                extracted_water += capacity
                capacity = 0
        
        return extracted_water

    # Main
    extractions = 0
    water = 0
    for row in grid:
        extractions += extract_water(row)
        water += extractions
    
    return math.ceil(water/capacity)

