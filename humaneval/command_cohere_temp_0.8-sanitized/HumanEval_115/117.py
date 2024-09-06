import math
class Bucket:
    def __init__(self, capacity):
        self.capacity = capacity
        self.filled_wells = 0

    def fill_well(self, well):
        """
        Fills the bucket from a well with given capacity
        """
        self.filled_wells += well <= self.capacity
        return self.filled_wells
def max_fill(grid, capacity):
    """
    Uses a bucket to empty the wells in the grid
    """
    bucket = Bucket(capacity)
    for row in grid:
        for well in row:
            if well == 1:
                bucket.fill_well(well)

    return bucket.filled_wells