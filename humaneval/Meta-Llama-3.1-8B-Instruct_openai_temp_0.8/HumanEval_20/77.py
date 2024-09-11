```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floats with a length of at least two.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in order.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # First, we sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # We initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[0])

    # We iterate over the sorted list of numbers to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        # We calculate the difference between the current number and the next number
        diff = sorted_numbers[i + 1] - sorted_numbers[i]

        # If the difference is less than the current minimum difference, we update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    # Finally, we return the closest pair of numbers
    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns the two closest numbers in the list. It sorts the list of numbers in ascending order and then iterates over the sorted list to find the closest pair of numbers by keeping track of the minimum difference between adjacent numbers. If the difference between two adjacent numbers is less than the current minimum difference, it updates the minimum difference and the closest pair. Finally, it returns the closest pair of numbers.