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
        Tuple[float, float]: A tuple of two numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Ensure the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = None

    # Iterate over all pairs
    for pair in pairs:
        # Calculate the difference between the two numbers in the pair
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

This script uses the `itertools.combinations` function to generate all possible pairs of numbers in the list. It then iterates over these pairs, calculates the difference between the two numbers in each pair, and keeps track of the pair with the smallest difference. Finally, it returns this closest pair. If two numbers in the list are equal, the script considers them the closest pair.