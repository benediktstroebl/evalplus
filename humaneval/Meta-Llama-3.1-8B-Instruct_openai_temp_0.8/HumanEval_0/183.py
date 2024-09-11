```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if there are any two numbers closer to each other than given threshold, False otherwise.
    """
    if len(numbers) < 2:
        # If there's less than 2 numbers, they cannot be close.
        return False

    # Sort the list to find close numbers
    numbers.sort()

    for i in range(1, len(numbers)):
        # For each two adjacent numbers
        if numbers[i] - numbers[i - 1] <= threshold:
            # If the distance is less than or equal to the threshold, return True
            return True

    # If no close numbers were found, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold. It sorts the list, and then checks each pair of adjacent numbers. If it finds two numbers with a distance less than or equal to the threshold, it returns True. If it checks all pairs and finds no such numbers, it returns False. The script also includes two test cases to demonstrate the function's behavior.