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
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Then, we iterate over the sorted list with the index and the next element
    for i in range(len(numbers) - 1):
        # For each element, we check if the difference with the next element is smaller than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If we find a pair of numbers with a difference smaller than the threshold, we return True
            return True
    
    # If we don't find any pair of numbers with a difference smaller than the threshold, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer to each other than a given threshold. It first sorts the list of numbers, then iterates over the sorted list to check the difference between each pair of adjacent numbers. If it finds a pair with a difference smaller than the threshold, it returns `True`. Otherwise, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.