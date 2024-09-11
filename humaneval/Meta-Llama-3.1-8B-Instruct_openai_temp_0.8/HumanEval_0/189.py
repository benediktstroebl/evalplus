### Close Elements Checker
#### Problem Description
Check if in a given list of numbers, there are any two numbers closer to each other than a specified threshold.

#### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list and check if the difference between each pair of adjacent numbers is less than the threshold
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i-1]) < threshold:
            return True
    
    # If no pair of adjacent numbers is closer than the threshold, return False
    return False

# Example usage:
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold value as input, sorts the list, and then checks each pair of adjacent numbers to see if their difference is less than the threshold. If any pair is closer than the threshold, the function returns `True`; otherwise, it returns `False`. The example usage at the end demonstrates how to use this function with some test cases.