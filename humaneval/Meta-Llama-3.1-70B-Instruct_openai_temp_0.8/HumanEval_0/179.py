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
    numbers.sort()  # Sort the list to apply the algorithm efficiently
    for i in range(len(numbers) - 1):  # Iterate over the sorted list
        if numbers[i + 1] - numbers[i] < threshold:  # Check the difference between adjacent numbers
            return True  # If the difference is less than the threshold, return True
    return False  # If no close elements are found, return False


# Test cases
if __name__ == "__main__":
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)  # Expected output: False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)  # Expected output: True
```

This script defines the `has_close_elements` function that takes a list of numbers and a threshold as input and returns `True` if any two numbers are closer than the threshold, and `False` otherwise. The function first sorts the list of numbers and then iterates over the sorted list to check the difference between adjacent numbers. If the difference is less than the threshold, the function returns `True`. If no close elements are found, the function returns `False`. The script also includes test cases to verify the functionality of the `has_close_elements` function.