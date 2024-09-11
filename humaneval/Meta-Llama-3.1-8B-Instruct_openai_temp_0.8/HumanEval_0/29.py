```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if there are two numbers closer to each other than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list
    for i in range(1, len(numbers)):
        # Check if the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i-1] < threshold:
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False

if __name__ == "__main__":
    # Test cases
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which takes a list of numbers and a threshold as input. It sorts the list of numbers and then iterates over the sorted list to check if the difference between any two consecutive numbers is less than the threshold. If such a pair is found, the function returns `True`. If no such pair is found after checking all numbers, the function returns `False`. The script also includes test cases to demonstrate the function's behavior.