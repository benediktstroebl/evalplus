```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance required between two numbers.

    Returns:
    bool: True if any two numbers are closer to each other than the threshold, False otherwise.
    """
    if len(numbers) < 2:  # List must have at least 2 elements to compare
        return False

    numbers.sort()  # Sort the list to simplify comparison

    for i in range(1, len(numbers)):
        # Calculate the distance between current and previous number
        distance = numbers[i] - numbers[i - 1]
        if distance < threshold:
            # If the distance is less than the threshold, return True
            return True

    # If no pairs of numbers are closer than the threshold, return False
    return False


# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list, then iterates over the sorted list to check the distance between each pair of adjacent numbers. If it finds a pair with a distance less than the threshold, it returns `True`; otherwise, it returns `False`.