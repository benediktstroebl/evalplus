```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered not close.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    if not numbers:  # edge case: empty list
        return False

    numbers.sort()  # sort the list to make it easier to find close elements
    for i in range(1, len(numbers)):
        # check if the difference between the current element and the previous one is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            return True
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script implements a simple function to check if there are any two numbers in a list that are closer together than a specified threshold. It first sorts the list of numbers, making it easier to check for close elements, and then iterates over the sorted list to find any two consecutive elements that are closer together than the threshold. If such elements are found, the function immediately returns True. If the loop completes without finding any close elements, the function returns False. The script also includes example usage of the function.