```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate through the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = abs(numbers[i] - numbers[i + 1])
        
        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True

    # If no pairs of numbers are closer than the threshold, return False
    return False


# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script works by first sorting the list of numbers in ascending order. It then iterates through the sorted list, calculating the difference between each pair of adjacent numbers. If it finds a pair of numbers with a difference less than or equal to the threshold, it immediately returns `True`. If it iterates through the entire list without finding any such pairs, it returns `False`.