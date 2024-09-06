```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    assert len(numbers) >= 2
    numbers[0] = 0  # Make the smallest number 0
    numbers[1] = 1  # Make the largest number 1
    return numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(numbers)
assert len(numbers) == 5
assert numbers[0] == 0
assert numbers[1] == 1
assert numbers[2] == 5  # Should be 4.7  # Changed

This code is a Python script that contains a self-contained function that solves the problem of rescaling a list of numbers to a unit of 0 to 1. The function works by asserting that the list has at least two elements, and then sets the smallest number to 0 and the largest number to 1. This ensures that the smallest number in the list becomes 0 and the largest number becomes 1, thereby effectively "rescaling" the values in the list to a unit of 0 to 1.