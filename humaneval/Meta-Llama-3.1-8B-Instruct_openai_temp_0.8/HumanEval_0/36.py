```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): A minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the given threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list
    for i in range(len(numbers) - 1):
        # If the difference between two consecutive numbers is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # Return True, indicating that the threshold is exceeded
            return True

    # If no two consecutive numbers exceed the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script first sorts the list of numbers, then iterates over the sorted list to check if any two numbers are closer than the given threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after checking all pairs, the function returns `False`.