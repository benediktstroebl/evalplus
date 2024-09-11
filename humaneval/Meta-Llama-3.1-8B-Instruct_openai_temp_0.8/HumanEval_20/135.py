```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of float numbers.

    Returns:
        Tuple[float, float]: A tuple of two float numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Ensure the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])

    # Iterate through the list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of float numbers as input and returns a tuple of two float numbers that are the closest to each other. The function first checks if the list has at least two elements, then sorts the list in ascending order. It iterates through the list to find the closest pair by keeping track of the minimum difference and updating it when a closer pair is found. Finally, it returns the closest pair. The script includes two test cases to demonstrate the function's usage.