```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list
    for i in range(1, len(numbers)):
        # If the difference between two adjacent numbers is less than the threshold, return True
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False

# Example usage:
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Two numbers are closer than the threshold")
else:
    print("No two numbers are closer than the threshold")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Two numbers are closer than the threshold")
else:
    print("No two numbers are closer than the threshold")
```

In this code, we first sort the list of numbers in ascending order. Then, we iterate over the sorted list and check if the difference between two adjacent numbers is less than the threshold. If we find any two numbers that are closer than the threshold, we return True immediately. If we finish iterating over the list without finding any such pair, we return False.