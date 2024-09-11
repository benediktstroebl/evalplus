```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers: A list of floats (of length at least two)

    Returns:
    A tuple of two floats, the closest pair of numbers in the list.

    Raises:
    ValueError: If the list has less than two elements
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = ()

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of floats as input and returns a tuple of the two closest numbers in the list. It first checks if the list has at least two elements, then sorts the list in ascending order. It then iterates over the sorted list to find the closest pair of numbers, keeping track of the minimum difference and the corresponding pair. Finally, it returns the closest pair.