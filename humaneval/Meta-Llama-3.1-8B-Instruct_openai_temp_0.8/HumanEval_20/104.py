```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of float numbers.

    Returns:
        A tuple of two float numbers that are the closest to each other.

    Raises:
        ValueError: If the length of the list is less than two.
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers.")

    numbers.sort()  # Sort the list to easily find the closest pair
    min_diff = float('inf')  # Initialize the minimum difference as infinity
    closest_pair = None  # Initialize the closest pair as None

    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            # If the current difference is smaller than the minimum difference, update the minimum difference and the closest pair
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of float numbers as input and returns a tuple of two float numbers that are the closest to each other. It first checks if the list contains at least two numbers. If not, it raises a `ValueError`. Then, it sorts the list and iterates over the sorted list to find the pair of numbers with the minimum difference. Finally, it returns the closest pair of numbers. The test cases are provided at the end of the script to demonstrate its usage.