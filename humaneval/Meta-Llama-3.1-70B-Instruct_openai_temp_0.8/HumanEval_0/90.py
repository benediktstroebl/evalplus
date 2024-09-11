```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers: A list of float numbers
    threshold: A float number that defines the minimum distance between two numbers

    Returns:
    bool: True if there are two numbers closer to each other than threshold, False otherwise
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Then, we iterate over the sorted list to compare the difference between adjacent numbers
    for i in range(len(numbers) - 1):
        # If the difference between two adjacent numbers is less than or equal to the threshold, we return True
        if numbers[i + 1] - numbers[i] <= threshold:
            return True
    
    # If we've iterated over the entire list and haven't found any two numbers closer to each other than the threshold, we return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```