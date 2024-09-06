Here is a self-contained Python function that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    # Sorting in ascending order
    numbers = sorted(numbers)
    # Current index
    i = 0
    # Count of equal numbers in the list
    equal_count = 0

    # Checking if any two numbers are closer than the threshold
    while i < len(numbers) - 1:
        if numbers[i] - numbers[i + 1] <= threshold:
            equal_count += 1
        i += 1

    # Checking if any two numbers are closer than the threshold
    return equal_count > 1
```
This function takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the threshold. It uses the sorting to arrange the list in ascending order, then, it iterates through the list and checks if any two consecutive elements are closer than the threshold. The function returns True if any two numbers in the list satisfy this condition.