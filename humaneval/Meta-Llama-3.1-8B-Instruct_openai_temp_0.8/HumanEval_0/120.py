### Close Elements Checker
#### Problem Description
Check if in a given list of numbers, any two numbers are closer to each other than a given threshold.

#### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance required between any two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # If the list has less than two elements, there are no pairs of numbers
    if len(numbers) < 2:
        return False

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the list of numbers (excluding the last one) and check each pair
    for i in range(len(numbers) - 1):
        # If the difference between the current number and the next one is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            return True

    # If no pairs were found with a distance less than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list of numbers in ascending order, then iterates over the list (excluding the last element) to check if any two consecutive numbers are closer than the threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after iterating over the entire list, the function returns `False`. The example usage at the end demonstrates the function's behavior with two different input lists.