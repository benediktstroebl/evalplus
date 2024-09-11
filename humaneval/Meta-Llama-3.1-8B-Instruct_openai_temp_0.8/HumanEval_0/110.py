```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered 'far'.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to easily compare adjacent elements
    for i in range(len(numbers) - 1):  # Iterate over the list, excluding the last element
        if abs(numbers[i] - numbers[i + 1]) <= threshold:  # Check if the current and next elements are closer than the threshold
            return True  # If they are, immediately return True
    return False  # If no pair of adjacent elements is closer than the threshold, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```