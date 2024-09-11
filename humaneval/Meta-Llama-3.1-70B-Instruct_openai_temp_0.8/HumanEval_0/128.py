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
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = abs(numbers[i] - numbers[i + 1])
        
        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True

    # If we have checked all pairs of numbers and haven't returned True, then no two numbers are closer than the threshold
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([10.0, 20.0, 30.0, 40.0, 50.0], 15.0))  # False
print(has_close_elements([10.0, 15.0, 20.0, 25.0, 30.0], 15.0))  # True
```