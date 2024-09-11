```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of numbers.
        threshold (float): The threshold to check.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.

    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    # First, sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Check if the difference between the current number and the previous number
        # is less than or equal to the threshold
        if numbers[i] - numbers[i - 1] <= threshold:
            # If it is, return True
            return True

    # If we've iterated over the entire list and haven't found any numbers that are
    # closer than the threshold, return False
    return False


# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a given threshold. The function sorts the list of numbers and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair of numbers that are closer than the threshold, it immediately returns `True`. If it iterates over the entire list without finding any such pair, it returns `False`.

The script also includes some test cases to demonstrate the function's behavior.