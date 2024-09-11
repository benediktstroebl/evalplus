Here's a Python script that solves the problem:


```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer to each other than the threshold, False otherwise.
    """
    if len(numbers) < 2:
        return False  # List must have at least two elements

    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] <= threshold:
            return True  # If the difference between two consecutive numbers is less than or equal to the threshold

    return False  # If no two numbers are closer than the threshold


# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script sorts the list of numbers and then checks each pair of consecutive numbers. If the difference between any two consecutive numbers is less than or equal to the threshold, it returns True. Otherwise, it returns False.