```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of float numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to simplify the comparison
    for i in range(len(numbers) - 1):  # Iterate over the list excluding the last element
        if numbers[i + 1] - numbers[i] <= threshold:  # Check if the difference between two consecutive numbers is less than or equal to the threshold
            return True
    return False  # If no pair of numbers is closer than the threshold, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the input list of numbers. It then iterates over the sorted list, checking for each pair of consecutive numbers if their difference is less than or equal to the given threshold. If such a pair is found, the function immediately returns `True`. If the function completes its iteration without finding a pair of numbers closer than the threshold, it returns `False`.