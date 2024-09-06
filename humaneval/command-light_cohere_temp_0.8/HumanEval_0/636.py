Here is a self-contained Python script with a function that checks if any two numbers in a given list are closer to each other than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold."""
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i+1] <= threshold:
            return True
    return False

# Test the function
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.3)
5.0, 2.0, 1.2]


# The output should be True as the numbers 2 and 1 are closer to each other than the threshold 0.0.

The function has been designed to operate on a list of floating-point numbers, and it returns a boolean value indicating whether any two numbers in the list are closer to each than the given threshold.