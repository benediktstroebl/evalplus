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
    bool: True if any two numbers are closer to each other than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list
    for i in range(len(numbers) - 1):
        # Check if the difference between the current and next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If it is, return True
            return True

    # If no pairs of numbers were found to be closer than the threshold, return False
    return False

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer to each other than a given threshold. It first sorts the list of numbers and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair that is closer than the threshold, it returns True. If it checks all pairs without finding any that are closer than the threshold, it returns False. The example usage at the end demonstrates how to use this function.