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
    numbers.sort()  # Sort the list in ascending order
    for i in range(1, len(numbers)):  # Iterate over the list starting from the second element
        if numbers[i] - numbers[i - 1] < threshold:  # Check if the difference between the current and previous elements is less than the threshold
            return True  # If it is, return True immediately
    return False  # If the loop completes without finding any pairs closer than the threshold, return False

# Example usage:
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("There are numbers closer than 0.5.")
else:
    print("No numbers are closer than 0.5.")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("There are numbers closer than 0.3.")
else:
    print("No numbers are closer than 0.3.")
```

This script sorts the list of numbers and then iterates over the sorted list. For each pair of adjacent elements, it checks if their difference is less than the given threshold. If it finds such a pair, it immediately returns `True`. If it finishes iterating over the list without finding any such pairs, it returns `False`.