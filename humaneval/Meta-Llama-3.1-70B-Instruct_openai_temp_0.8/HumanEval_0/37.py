```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum difference between two numbers.

    Returns:
        bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with the index and value
    for i in range(len(numbers) - 1):
        # For each number, we calculate the difference with the next number
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, we return True
        if difference <= threshold:
            return True

    # If we have iterated over the entire list and haven't found any close elements, we return False
    return False


# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function which checks if there are any two numbers in the given list that are closer to each other than the given threshold. It first sorts the list of numbers in ascending order and then iterates over the sorted list, calculating the difference between each number and the next one. If it finds a difference that is less than or equal to the threshold, it immediately returns `True`. If it iterates over the entire list without finding any close elements, it returns `False`. The script also includes two test cases to demonstrate the function's behavior.