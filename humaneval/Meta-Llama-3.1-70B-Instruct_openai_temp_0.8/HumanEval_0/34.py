```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Calculate the absolute difference between the current number and the previous one
        difference = abs(numbers[i] - numbers[i-1])
        
        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True

    # If no pair of numbers with a difference less than or equal to the threshold is found, return False
    return False


# Example use cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```