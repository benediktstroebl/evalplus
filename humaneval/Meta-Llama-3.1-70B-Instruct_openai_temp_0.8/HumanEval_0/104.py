```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks if in the given list of numbers, are any two numbers closer to each other than the given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list in ascending order
    numbers.sort()
    
    # Then, we iterate over the sorted list
    for i in range(len(numbers) - 1):
        # For each number, we check the distance to the next number
        if numbers[i + 1] - numbers[i] < threshold:
            # If the distance is less than the threshold, we return True
            return True
    
    # If we have checked all numbers and haven't found any that are closer than the threshold, we return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```