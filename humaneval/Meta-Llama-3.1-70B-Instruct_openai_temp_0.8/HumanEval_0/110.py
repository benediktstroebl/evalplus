```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The maximum allowed difference between any two numbers.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with a for loop that has access to both the index and the value
    for i, num in enumerate(numbers):
        # For the first number in the list, we can't check the difference with the previous number, so we skip it
        if i == 0:
            continue

        # For each number, we calculate the difference with the previous number
        difference = num - numbers[i - 1]

        # If the difference is less than or equal to the threshold, we return True
        if difference <= threshold:
            return True

    # If we've iterated over the entire list and haven't found any numbers closer than the threshold, we return False
    return False


# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if there are any two numbers in the input list that are closer to each other than the given threshold. The function first sorts the list of numbers, then iterates over the sorted list to check the difference between each number and its predecessor. If it finds any two numbers with a difference less than or equal to the threshold, it immediately returns `True`. If it iterates over the entire list without finding any such pair of numbers, it returns `False`. The script also includes some test cases to demonstrate the function's behavior.