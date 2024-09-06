Here's a Python script that solves the problem using a nested for loop and a simple `Counter` class to keep track of the wells that can be filled:
```python
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

# Test the function
if __name__ == "__main__":
    test_cases = [
        ([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1, 6),
        ([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2, 5),
        ([[0, 0, 0], [0, 0, 0]], 5, 0)
    ]

    for grid, capacity, expected in test_cases:
        result = max_fill(grid, capacity)
        assert result == expected, f"Expected {expected} but got {result}"
```

The `Bucket` class has a `fill_well` method that counts the number of wells that can be filled with the given `capacity`. The method is called within the `max_fill` function, which creates a `Bucket` instance and uses nested loops to iterate through every `well` in the `grid`. If a `well` is filled with `1`, the `fill_well` method is used to count the number of wells that can be filled by that well. Finally, the function returns the total number of wells that can be filled.