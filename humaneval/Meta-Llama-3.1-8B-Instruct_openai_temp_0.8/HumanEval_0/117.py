```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the list, checking each pair of adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between two adjacent numbers is less than the threshold, return True
        if numbers[i] - numbers[i-1] < threshold:
            return True

    # If no pairs of adjacent numbers are closer than the threshold, return False
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

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns True if any two numbers in the list are closer than the threshold, and False otherwise. The function first sorts the list of numbers, then iterates over the list, checking each pair of adjacent numbers to see if they are closer than the threshold. If any pair is closer, the function returns True; otherwise, it returns False. The script also includes two test cases to verify that the function is working correctly.