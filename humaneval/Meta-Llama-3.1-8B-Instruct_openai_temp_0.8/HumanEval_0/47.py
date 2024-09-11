```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to consider them close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list, checking each pair of adjacent elements
    for i in range(1, len(numbers)):
        # If the difference between the current element and the previous element is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            # Return True, because we've found two elements that are closer than the threshold
            return True

    # If we've iterated over the entire list and found no pairs of elements that are closer than the threshold
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```