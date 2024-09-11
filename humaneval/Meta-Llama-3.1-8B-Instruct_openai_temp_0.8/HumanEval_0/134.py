### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers in the list are closer to each other than the given threshold, False otherwise.
    """
    # If the list has less than 2 elements, there can't be any close elements
    if len(numbers) < 2:
        return False

    # Iterate over the list of numbers
    for i in range(len(numbers) - 1):
        # Check if the current number and the next number are closer than the threshold
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True

    # If we've checked all pairs of numbers and haven't found any close ones, return False
    return False


# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. The function iterates over the list of numbers, checking each pair of adjacent numbers to see if they are closer than the threshold. If it finds any pair of close numbers, it immediately returns `True`. If it checks all pairs of numbers without finding any close ones, it returns `False`. The script also includes example usage to demonstrate how to call the function.