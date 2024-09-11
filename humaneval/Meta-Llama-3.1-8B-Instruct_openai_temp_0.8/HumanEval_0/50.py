```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered "close".

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Create a set to store numbers we have seen so far
    seen = set()

    # Iterate over the list of numbers
    for num in numbers:
        # For each number, find the distance to all previously seen numbers
        for prev_num in seen:
            # If the distance between the current number and a previously seen number is less than the threshold
            if abs(num - prev_num) < threshold:
                # Return True, we have found two numbers that are closer than the threshold
                return True
        # Add the current number to the set of seen numbers
        seen.add(num)

    # If we have iterated over all numbers and haven't found any pair of numbers that are closer than the threshold
    # Return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It iterates over the list of numbers and for each number, it checks the distance to all previously seen numbers. If it finds two numbers that are closer than the threshold, it returns True. If it iterates over all numbers and doesn't find any pair of numbers that are closer than the threshold, it returns False. The script also includes test cases to verify the correctness of the function.