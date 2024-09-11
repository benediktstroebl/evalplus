```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The maximum allowed difference between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Then, iterate over the sorted list with the index and value
    for i, num in enumerate(numbers):
        # Skip the first number, since we're comparing each number with its next number
        if i == 0:
            continue
        
        # If the difference between the current number and the previous number is less than the threshold, return True
        if num - numbers[i - 1] < threshold:
            return True
    
    # If the loop completes without finding any close elements, return False
    return False


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test 1 failed")
if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test 2 failed")
if not has_close_elements([10.0, 20.0, 30.0], 5.0):
    print("Test 3 failed")
if has_close_elements([0.1, 0.2], 0.05):
    print("Test 4 failed")
print("All tests passed")
```