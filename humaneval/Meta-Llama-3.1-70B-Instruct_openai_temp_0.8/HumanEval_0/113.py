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
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # For each number, check if the difference with the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If a difference less than the threshold is found, return True
            return True
    
    # If no differences less than the threshold are found, return False
    return False


# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the sorting approach, which has a time complexity of O(n log n), where n is the number of elements in the list. This is because the sorting operation dominates the time complexity of this solution.