```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between any two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    if len(numbers) < 2:
        # A list with less than two elements cannot have two numbers closer than a threshold.
        return False

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Compare each pair of numbers in the list.
            if abs(numbers[i] - numbers[j]) < threshold:
                # If a pair of numbers is closer than the threshold, return True.
                return True

    # If no pair of numbers is closer than the threshold, return False.
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1: Expected False, but got True")
else:
    print("Test case 1: Expected False, and got False")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2: Expected True, and got True")
else:
    print("Test case 2: Expected True, but got False")
```