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
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list, comparing each number with its next neighbor
    for i in range(len(numbers) - 1):
        # If the difference between two adjacent numbers is less than the threshold, return True
        if numbers[i + 1] - numbers[i] < threshold:
            return True

    # If no pair of numbers closer than the threshold is found, return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

Alternatively, you could also use a more concise version using the `min` function and a generator expression:

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
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    return min((abs(x - y) for i, x in enumerate(numbers) for y in numbers[i + 1:]), default=float('inf')) < threshold


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

However, this version has a time complexity of O(n^2), whereas the first version has a time complexity of O(n log n) due to the sorting step.