```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Iterate over the list from the second element to the last element
    for i in range(1, len(numbers)):
        # Check if the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            # If it is, return True
            return True
    
    # If the loop completes without finding any pair of numbers closer than the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the list of numbers in ascending order. Then it checks each pair of adjacent numbers to see if they are closer than the given threshold. If it finds such a pair, it immediately returns True. If it checks all pairs without finding any closer than the threshold, it returns False.