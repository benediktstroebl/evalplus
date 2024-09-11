```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers: A list of floating point numbers.
        threshold: The minimum difference required between two numbers.

    Returns:
        True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list to compare each number with its neighbors
    for i in range(1, len(numbers)):
        # Check if the difference between current number and its previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True

    # If we have iterated over the entire list without finding any two numbers closer than the threshold, return False
    return False


# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.6))  # False
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, sorts the list, and then iterates over it to find any two adjacent numbers whose difference is less than the threshold. If such a pair is found, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to demonstrate the function's behavior.