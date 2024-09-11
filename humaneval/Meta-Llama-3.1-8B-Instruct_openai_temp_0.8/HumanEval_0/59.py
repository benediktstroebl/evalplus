```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to consider them close.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(sorted_numbers)):
        # If the current number and the previous number have a distance less than the threshold
        if sorted_numbers[i] - sorted_numbers[i-1] < threshold:
            # Return True, indicating that we've found two numbers that are closer than the threshold
            return True
    
    # If we've iterated over the entire list and haven't found any two numbers that are closer than the threshold, return False
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 failed")
else:
    print("Test case 1 passed")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 failed")
else:
    print("Test case 2 passed")
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold value, and returns a boolean value indicating whether any two numbers in the list are closer than the threshold. The function sorts the list of numbers and then iterates over the sorted list, checking the distance between each pair of adjacent numbers. If it finds a pair of numbers with a distance less than the threshold, it returns True. Otherwise, it returns False. The script includes two test cases to verify the correctness of the function.