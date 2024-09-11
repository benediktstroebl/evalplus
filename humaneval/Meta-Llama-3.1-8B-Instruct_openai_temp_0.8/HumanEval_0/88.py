```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    if len(numbers) < 2:
        return False  # If there are less than two numbers, no two numbers can be close

    numbers.sort()  # Sort the numbers in ascending order
    for i in range(len(numbers) - 1):
        # Calculate the difference between each pair of adjacent numbers
        diff = numbers[i + 1] - numbers[i]
        if diff <= threshold:
            return True  # If the difference is less than or equal to the threshold, return True

    return False  # If no pair of adjacent numbers are within the threshold, return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It sorts the list of numbers and then checks each pair of adjacent numbers to see if their difference is less than or equal to the threshold. If it finds such a pair, it immediately returns `True`. If it checks all pairs of adjacent numbers and finds no pairs within the threshold, it returns `False`. The script also includes test cases to verify the correctness of the function.