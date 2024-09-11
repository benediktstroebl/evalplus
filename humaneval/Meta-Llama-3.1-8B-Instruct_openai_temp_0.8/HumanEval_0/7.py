```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of floating point numbers.
        threshold (float): Minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Iterate through the sorted list and check the distance between adjacent numbers
    for i in range(len(sorted_numbers) - 1):
        distance = sorted_numbers[i + 1] - sorted_numbers[i]
        if distance <= threshold:
            return True

    return False


# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
    print(has_close_elements([1.0, 2.0, 3.0], 1.0))  # False
    print(has_close_elements([1.0, 3.0, 5.0], 1.0))  # False
    print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 1.0))  # True
```
This script defines a function `has_close_elements` that sorts the list of numbers and then checks the distance between adjacent numbers. If any distance is less than or equal to the threshold, the function returns `True`. Otherwise, it returns `False`. The script also includes test cases to verify the correctness of the function.