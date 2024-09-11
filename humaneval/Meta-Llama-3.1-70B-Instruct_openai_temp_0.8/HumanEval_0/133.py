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
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum distance to a value larger than the threshold
    min_distance = float('inf')

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Calculate the distance between the current number and the previous one
        distance = numbers[i] - numbers[i - 1]
        
        # Update the minimum distance if the current distance is smaller
        min_distance = min(min_distance, distance)

    # Return True if the minimum distance is smaller than the threshold, False otherwise
    return min_distance < threshold


# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function as specified, sorts the list of numbers, and then iterates over the sorted list to find the minimum distance between any two numbers. If the minimum distance is smaller than the threshold, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to verify the correctness of the function.