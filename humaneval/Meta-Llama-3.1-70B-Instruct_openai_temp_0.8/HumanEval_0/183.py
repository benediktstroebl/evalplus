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
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.

    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list, checking the difference between each pair of adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between two numbers is less than or equal to the threshold, return True
        if numbers[i] - numbers[i-1] <= threshold:
            return True
    
    # If no pairs of numbers are closer than the threshold, return False
    return False


# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print True
```
This script defines the `has_close_elements` function and includes example use cases in the docstring. It then tests the function with the provided examples and prints the results.