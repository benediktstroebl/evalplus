```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum difference required between two numbers.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Create a copy of the list and sort it
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list to find any adjacent numbers with a difference less than the threshold
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:
            return True
    
    # If no such pair is found, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```