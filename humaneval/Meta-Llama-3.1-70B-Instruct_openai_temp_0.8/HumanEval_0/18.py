```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # If the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            # Return True, indicating that two numbers are closer than the threshold
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False


# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This Python script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. The function sorts the list of numbers and then iterates over the sorted list, checking the difference between each pair of adjacent numbers. If it finds a pair of numbers that are closer than the threshold, it immediately returns `True`. If it checks all pairs of numbers without finding any that are closer than the threshold, it returns `False`. The script also includes two test cases to demonstrate its usage.