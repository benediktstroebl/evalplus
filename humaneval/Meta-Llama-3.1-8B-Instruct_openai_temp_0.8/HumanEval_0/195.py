### Has Close Elements Solution

Here's a Python script that implements the `has_close_elements` function:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance for two numbers to be considered close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list, checking each pair of adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference between two adjacent numbers is less than the threshold, return True
        if numbers[i] - numbers[i - 1] < threshold:
            return True

    # If we've checked all pairs of adjacent numbers and haven't found any that are too close, return False
    return False


# Example usage:
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the list of numbers, then iterates over the list, checking each pair of adjacent numbers to see if their difference is less than the given threshold. If it is, the function immediately returns True. If it checks all pairs of adjacent numbers without finding any that are too close, it returns False.