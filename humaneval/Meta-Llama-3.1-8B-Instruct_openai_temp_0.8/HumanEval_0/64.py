### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers are within the given threshold, False otherwise.
    """
    # Create a copy of the list, sort it in ascending order, and remove duplicates
    sorted_numbers = sorted(set(numbers))
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(sorted_numbers)):
        # Check if the distance between the current number and the previous number is less than the threshold
        if sorted_numbers[i] - sorted_numbers[i-1] < threshold:
            return True
    
    # If no pair of numbers is within the threshold, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

### Explanation
This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold value as input. It first creates a sorted list of unique numbers by converting the input list to a set and sorting it. Then, it iterates over this list to check if the distance between any two consecutive numbers is less than the given threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after iterating over the entire list, the function returns `False`.