```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If it is, return True
            return True

    # If no close elements are found, return False
    return False


# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```

This code defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns `True` if any two numbers in the list are closer to each other than the threshold, and `False` otherwise. The function uses a simple sorting and iteration approach to check for close elements. The example usage at the end demonstrates how to call the function with different inputs.