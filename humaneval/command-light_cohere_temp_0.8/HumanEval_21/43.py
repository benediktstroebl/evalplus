```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation to the numbers in the list
    numbers_res = [x / 100.0 for x in numbers]
    # Return the list of rescaled numbers
    return numbers_res

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(numbers)

This function takes a list of numbers as input and applies a linear transformation to the numbers in the list, such that the smallest number will become 0 and the largest will become 1. The function then returns a list of rescaled numbers.