```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The threshold distance.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Then, we iterate over the sorted list with a for loop and its index
    for i in range(len(numbers) - 1):
        # For each number, we calculate the difference with the next number
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, we return True
        if difference <= threshold:
            return True
    
    # If we have iterated over the entire list and haven't found any pair of numbers
    # closer than the threshold, we return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer than a given threshold. The function first sorts the list of numbers, then iterates over the sorted list to check the difference between each pair of adjacent numbers. If it finds a pair of numbers closer than the threshold, it immediately returns `True`. If it iterates over the entire list without finding such a pair, it returns `False`. The script also includes two test cases to demonstrate the function's usage.