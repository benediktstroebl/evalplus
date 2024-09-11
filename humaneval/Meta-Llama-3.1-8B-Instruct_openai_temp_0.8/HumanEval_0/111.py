```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum difference between two numbers to be considered close.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list to check for close elements
    for i in range(1, len(numbers)):
        # If the difference between two consecutive numbers is less than the threshold, return True
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    
    # If no close elements are found, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as inputs. It sorts the list in ascending order and then checks for pairs of numbers that are closer than the threshold by iterating over the sorted list. If it finds any such pair, it returns `True`. If no such pair is found, it returns `False`. The example usage demonstrates the function's behavior with the provided test cases.