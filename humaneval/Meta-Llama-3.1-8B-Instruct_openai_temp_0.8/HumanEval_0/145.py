```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum difference between two numbers to be considered close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list of numbers in ascending order
    for i in range(1, len(numbers)):  # Iterate over the list starting from the second element
        if numbers[i] - numbers[i-1] <= threshold:  # Check if the difference is less than or equal to the threshold
            return True  # If yes, return True immediately
    return False  # If no close elements are found, return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. It sorts the list and then iterates over it, checking if the difference between each pair of adjacent numbers is less than or equal to the threshold. If such a pair is found, the function returns True; otherwise, it returns False. The script also includes example usage of the function.