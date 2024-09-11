Here's a self-contained Python script that solves the given problem:

```markdown
### Problem: Check if Two Numbers are Closer than a Threshold in a List

### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    numbers.sort()  # Sort the list to easier to find close numbers
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] <= threshold:
            return True  # If difference is less than or equal to threshold, return True
    return False  # If no close numbers found, return False

### Example Usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

### Explanation

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer than a given threshold. It sorts the list to make it easier to find close numbers, then iterates over the sorted list, checking the difference between each pair of consecutive numbers. If it finds a pair with a difference less than or equal to the threshold, it immediately returns `True`. If it iterates over the entire list without finding any close numbers, it returns `False`. The script also includes example usage to demonstrate the function's behavior.