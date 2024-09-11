### Close Elements Checker
#### Problem Statement
Check if in given list of numbers, are any two numbers closer to each other than given threshold.

#### Solution
Here's a Python function `has_close_elements` that solves the problem:

```markdown
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): A float value that represents the minimum distance between two numbers.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list
    for i in range(1, len(numbers)):
        # Check if the difference between the current number and the previous number is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            return True

    # If the loop completes without finding two numbers closer than the threshold, return False
    return False


# Example use cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold value. It sorts the list of numbers, then iterates over the sorted list to check if the difference between consecutive numbers is less than the threshold. If it finds two numbers closer than the threshold, it returns `True`. Otherwise, it returns `False`. The script also includes example use cases to demonstrate how to use the function.