### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # If the list has less than two elements, we cannot have two elements closer than the threshold
    if len(numbers) < 2:
        return False

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list and check for any two adjacent elements closer than the threshold
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] <= threshold:
            return True

    # If no two adjacent elements are closer than the threshold, check for any two non-adjacent elements
    for i in range(len(numbers)):
        for j in range(i + 2, len(numbers)):
            if abs(numbers[j] - numbers[i]) <= threshold:
                return True

    # If no two elements are closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

### Explanation

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It first checks if the list has less than two elements, in which case it returns False because we cannot have two elements closer than the threshold.

Then it sorts the list of numbers in ascending order. It iterates over the sorted list and checks for any two adjacent elements closer than the threshold. If it finds any, it immediately returns True.

If no two adjacent elements are closer than the threshold, it checks for any two non-adjacent elements by iterating over the list and checking for any element that is closer than the threshold to any element two positions ahead. If it finds any, it immediately returns True.

If no two elements are closer than the threshold after checking both adjacent and non-adjacent elements, it returns False.