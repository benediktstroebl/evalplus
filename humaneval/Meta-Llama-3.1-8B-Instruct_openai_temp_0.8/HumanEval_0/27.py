```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between any two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks for any two numbers in the given list that are closer to each other than the specified threshold. It uses a nested loop to compare each pair of numbers and returns `True` as soon as it finds a pair that is closer than the threshold. If no such pair is found after checking all pairs, it returns `False`. The example usage shows how to use the function with the provided test cases.