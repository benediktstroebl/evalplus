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
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to bring closest numbers together
    for i in range(len(numbers) - 1):  # Iterate over the sorted list
        if numbers[i + 1] - numbers[i] < threshold:  # Check if adjacent numbers are closer than the threshold
            return True
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test 1 failed")
if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test 2 failed")
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a given threshold. The function sorts the list and then iterates over it to check if adjacent numbers are closer than the threshold. If it finds such a pair, it immediately returns `True`. If it doesn't find any such pair after checking all numbers, it returns `False`. The script also includes two test cases to verify that the function works correctly.