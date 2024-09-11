```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
    bool: True if any two numbers are closer to each other than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list to check for close elements
    for i in range(1, len(numbers)):
        # Calculate the distance between the current element and the previous one
        distance = numbers[i] - numbers[i - 1]
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True

    # If no close elements were found, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, sorts the list in ascending order, and then checks each pair of adjacent elements to see if their distance is less than the threshold. If such a pair is found, the function immediately returns `True`; otherwise, it returns `False`. The example usage demonstrates the function's behavior with the provided test cases.