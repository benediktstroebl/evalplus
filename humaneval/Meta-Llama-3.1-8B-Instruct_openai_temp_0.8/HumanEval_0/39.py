### Problem Solution

Here's a Python script that solves the problem using the given function.

```markdown
### Code
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the given threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list to check for close elements
    for i in range(len(numbers) - 1):
        # Check if the difference between two adjacent numbers is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            return True

    # If no close elements are found, return False
    return False

### Example Usage
if __name__ == "__main__":
    # Test the function with example inputs
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

### Explanation

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. The function sorts the list of numbers and then iterates over the sorted list to check for adjacent numbers with a difference less than the threshold. If such a pair is found, the function returns `True`; otherwise, it returns `False`. The script also includes example usage of the function.