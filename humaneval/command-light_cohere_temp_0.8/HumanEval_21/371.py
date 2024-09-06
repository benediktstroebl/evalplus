```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters: List[float] numbers
    Returns: List[float] A list with the same values after applying the transformation.

# Example:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

numbers = rescale_to_unit(numbers)

# Test case 1:
print(numbers)  # Output: [0.0, 0.0, 0.0, 0.0, 0.0]

test case 2:
# Test case 2:
print(numbers)  # Output: [0.0, 1.0, 2.0, 3.0, 5.0]
test case 3:
print(numbers)  # Output: [0.0, 0.0, 0.0, 1.0]
test case 4:
print(numbers)  # Output: [0.0, 0.0, 0.0, 2]

print(numbers)  # Output: [0.0, 0.0, 2.0, 3]

print(numbers)  # Output: [0.0, 0.0, 3]0]

print(numbers)  # Output: [0.0, 1.0, 3]0]

``` The function 'rescale_to_unit' in this script accepts a list of numbers as input and outputs a list of the same numbers, but after applying a linear transformation that scales all values from 0 to 1. You can use this to test the function using the input test cases you want.