```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance required between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Calculate the distance between the current number and the previous number
        distance = numbers[i] - numbers[i - 1]
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True

    # If no pair of numbers are closer than the threshold, return False
    return False


# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input, and returns `True` if any two numbers in the list are closer than the threshold, and `False` otherwise. The function first sorts the list of numbers, and then iterates over the sorted list to calculate the distance between each pair of adjacent numbers. If a distance is found to be less than the threshold, the function immediately returns `True`. If no such distance is found after iterating over the entire list, the function returns `False`. The example usage demonstrates the function's behavior with two different input lists.