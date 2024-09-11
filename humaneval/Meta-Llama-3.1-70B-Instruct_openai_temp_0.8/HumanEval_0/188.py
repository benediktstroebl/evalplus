```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to efficiently compare adjacent elements
    for i in range(len(numbers) - 1):  # Iterate over the sorted list
        if numbers[i + 1] - numbers[i] < threshold:  # Check if the difference is less than the threshold
            return True  # If it is, return True
    return False  # If no such pair is found, return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which takes a list of float numbers and a threshold as input. It sorts the list, then iterates over the sorted list to check if the difference between any two adjacent elements is less than the threshold. If such a pair is found, the function returns True. Otherwise, it returns False.

The script also includes two test cases to demonstrate the function's behavior.