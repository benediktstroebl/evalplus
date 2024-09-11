```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
    bool: True if any two numbers in the list are closer than the given threshold, False otherwise.
    """
    numbers.sort()  # Sort the list in ascending order to simplify the comparison
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] < threshold:  # Check if current number is close to the previous one
            return True
    return False  # If no close elements found, return False

# Example use cases:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This Python script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list, then iterates over the sorted list to check if any two adjacent numbers are closer than the given threshold. If such a pair is found, the function returns True; otherwise, it returns False.