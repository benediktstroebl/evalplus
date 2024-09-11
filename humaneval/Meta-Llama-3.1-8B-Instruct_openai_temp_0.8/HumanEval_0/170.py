```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers in the list are closer to each other than the threshold, False otherwise.
    """
    num_elements = len(numbers)
    for i in range(num_elements):
        for j in range(i + 1, num_elements):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False

# Example use cases:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This Python script defines a function `has_close_elements` that checks if any two numbers in the list are closer to each other than the given threshold. It uses a nested for loop to compare each pair of numbers in the list. If it finds a pair of numbers that are closer to each other than the threshold, it immediately returns `True`. If it checks all pairs of numbers without finding any close ones, it returns `False`.