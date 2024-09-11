```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): The list of numbers to check.
        threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False


# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer than a specified threshold. The function uses a nested loop to compare each pair of numbers in the list, and returns `True` as soon as it finds a pair that is closer than the threshold. If it checks all pairs without finding one that is closer, it returns `False`. The example usage at the end demonstrates how to use this function with the provided test cases.