```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered far enough.

    Returns:
    bool: True if any two numbers are closer to each other than threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to compare adjacent numbers
    for i in range(1, len(numbers)):
        # Check if the difference between current and previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script defines a function `has_close_elements` that sorts the list of numbers and then checks each pair of adjacent numbers to see if their difference is less than the given threshold. If it finds such a pair, it immediately returns `True`. If it checks all pairs without finding one that's too close, it returns `False`. The example usage at the end shows how to use this function with the provided test cases.