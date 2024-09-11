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
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If the numbers are close, return True
            return True

    # If no close numbers are found, return False
    return False

# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer than a specified threshold. The function sorts the list of numbers and then iterates over the sorted list to check the difference between each pair of adjacent numbers. If a pair of numbers is found to be closer than the threshold, the function returns `True`. Otherwise, it returns `False`. The script includes test cases to demonstrate the function's behavior.