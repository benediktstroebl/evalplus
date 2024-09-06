Here's the solution:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    # Ensure the necessary is at least two numbers
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers.")

    # Apply the linear transformation to numbers, and return the result
    return [num / float(numbers[1] - numbers[0]) for num in numbers]

# Test cases:
numbers = [1.0, 2.0, 3.0, 4.0, 0.0]
print_output = [0.0, 0.0, 0.0, 0.0]
print_test = [rescale_to_unit(numbers)]

This Python code defines a function called rescale_to_unit that takes a list of numbers as input and applies a linear transformation to the input list. The function ensures that the input list contains at least two numbers and then rescales the numbers based on the difference between the first and last elements in the list.