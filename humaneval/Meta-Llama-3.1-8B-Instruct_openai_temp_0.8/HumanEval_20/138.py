```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other
    and return them in order (smaller number, larger number).

    Args:
        numbers: A list of at least two float numbers.

    Returns:
        A tuple of two numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Initialize the minimum difference and the pair of elements with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = None

    # Iterate over the list to consider each pair of elements
    for i in range(len(numbers)):
        # Check the next element
        if i < len(numbers) - 1:
            # Calculate the absolute difference between the current element and the next one
            diff = abs(numbers[i] - numbers[i + 1])
            # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[i + 1])

    # Return the pair of elements with the minimum difference
    return closest_pair

print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two numbers that are the closest to each other. The function iterates over the list to consider each pair of elements and keeps track of the pair with the minimum difference found so far. The script also includes two example calls to the function.