```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers for them to be considered close.

    Returns:
    bool: True if there are two numbers closer to each other than the given threshold, False otherwise.
    """
    # First, sort the list of numbers
    numbers.sort()
    
    # Iterate over the list of numbers, checking each pair of adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between the current and previous number is less than the threshold, return True
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    
    # If we've checked all pairs of numbers and haven't found any that are closer than the threshold, return False
    return False

# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the list of numbers, then iterates over the sorted list to check each pair of adjacent numbers. If it finds two numbers that are closer than the given threshold, it immediately returns `True`. If it checks all pairs of numbers without finding any that are closer than the threshold, it returns `False`.