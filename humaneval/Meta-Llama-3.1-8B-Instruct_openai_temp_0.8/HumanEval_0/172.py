```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The threshold value.

    Returns:
        bool: True if any two numbers are closer, False otherwise.

    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Iterate over the sorted list
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If it is, return True
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False

# Example usage
numbers1 = [1.0, 2.0, 3.0]
threshold1 = 0.5
print(has_close_elements(numbers1, threshold1))  # Output: False

numbers2 = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
threshold2 = 0.3
print(has_close_elements(numbers2, threshold2))  # Output: True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold value as input. It sorts the list, then iterates over the sorted list to check if any two consecutive numbers are closer than the threshold. If it finds such a pair, it immediately returns `True`. If it checks all pairs without finding any that are closer than the threshold, it returns `False`.