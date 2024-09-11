```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list, checking each element with its next one
    for i in range(len(numbers) - 1):
        # If the difference between the current element and the next one is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # Return True, indicating that two numbers are closer than the threshold
            return True
    
    # If the function hasn't returned True after checking all pairs, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([10.0, 12.0, 15.0, 18.0], 2.0))  # False
print(has_close_elements([1.0, 1.1, 1.2, 1.3, 1.4], 0.3))  # True
```