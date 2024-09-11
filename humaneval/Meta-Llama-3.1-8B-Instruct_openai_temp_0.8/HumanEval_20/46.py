```python
from typing import List, Tuple
import itertools


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing two numbers from the list that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Generate all possible pairs of numbers from the list
    pairs = list(itertools.combinations(numbers, 2))

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = None

    # Iterate over all pairs
    for pair in pairs:
        # Calculate the absolute difference between the two numbers
        diff = abs(pair[0] - pair[1])

        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair

    # Return the closest pair
    return tuple(sorted(closest_pair))


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

In this script, we first check if the list has at least two elements. We then generate all possible pairs of numbers from the list using `itertools.combinations`. We iterate over all pairs, calculate the absolute difference between the two numbers, and update the minimum difference and the closest pair if a smaller difference is found. Finally, we return the closest pair, sorted in order.