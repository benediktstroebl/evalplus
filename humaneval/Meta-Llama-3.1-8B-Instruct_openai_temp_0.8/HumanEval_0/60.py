```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers in the list are closer to each other than the threshold, False otherwise.
    """
    # Sort the list in ascending order to bring close elements together
    numbers.sort()

    # Iterate over the sorted list to compare each number with its next one
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next one is smaller than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If the difference is smaller, return True
            return True

    # If the loop completes without finding any pair of close elements, return False
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

In this script, the function `has_close_elements` takes a list of floating point numbers and a threshold value as input. It sorts the list in ascending order, then iterates over the sorted list to compare each number with its next one. If the difference between any two adjacent numbers is smaller than the threshold, the function immediately returns True. If the loop completes without finding any pair of close elements, the function returns False. The example usage at the end demonstrates how to use this function to solve the problem.