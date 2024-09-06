Here's the self-contained Python script that solves the problem:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    5.5) are80000
   5.1, 8.0, 4.5, 0.3, 2.5, 0.0, 4), 0) are any numbers that have any two numbers closer to each other than given threshold.
    return:
    return any(numbers[0] < numbers[1] - threshold and numbers[1] < numbers[0] - threshold)


# Test the function with a sample
test_has_close_elements([1.0, 2.0, 3.0, 0.0, 5.5])

print(has_close_elements(test_has_close_elements([1.0, 2.0, 3.0, 0.5, 0.5, 5.0, 0.1, 8)) is True

```