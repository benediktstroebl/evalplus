```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of numbers of length at least two.

    Returns:
        A tuple of two numbers that are the closest to each other in the input list.
    """

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the corresponding pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()

    # Iterate through the sorted list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the closest pair of numbers
    return closest_pair


# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns the closest pair of numbers in the list. The function first sorts the input list in ascending order, then iterates through the sorted list to find the closest pair of numbers. The closest pair is updated whenever a smaller difference is found. The function returns the closest pair of numbers as a tuple. The script includes example usage and docstrings to demonstrate the function's behavior.