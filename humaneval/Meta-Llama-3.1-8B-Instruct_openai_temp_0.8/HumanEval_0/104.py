```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers in the list are closer to each other than the given threshold, False otherwise.
    """
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted numbers
    for i in range(len(sorted_numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if sorted_numbers[i + 1] - sorted_numbers[i] < threshold:
            return True
    
    # If no close elements are found, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, sorts the numbers, and checks if any two consecutive numbers are closer to each other than the threshold. The function returns True if any close elements are found and False otherwise. The script includes example usage of the function with the provided test cases.