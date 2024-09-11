```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers for them to be considered different.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate through the sorted list, checking each pair of adjacent elements
    for i in range(len(numbers) - 1):
        # If the difference between the two elements is less than or equal to the threshold, return True
        if numbers[i + 1] - numbers[i] <= threshold:
            return True
    
    # If we've checked all pairs of adjacent elements and haven't found any with a difference <= threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```