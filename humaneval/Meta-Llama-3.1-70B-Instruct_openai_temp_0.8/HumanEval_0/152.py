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

    # First, we sort the list of numbers in ascending order.
    # This is done to ensure that we can compare adjacent numbers in the list,
    # which will be the closest to each other.
    numbers.sort()

    # We then iterate over the sorted list of numbers.
    for i in range(len(numbers) - 1):
        # For each number, we calculate the absolute difference with the next number.
        difference = abs(numbers[i] - numbers[i + 1])
        
        # If the difference is less than or equal to the threshold, we return True.
        if difference <= threshold:
            return True

    # If we have iterated over the entire list and haven't found any numbers closer
    # than the threshold, we return False.
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```