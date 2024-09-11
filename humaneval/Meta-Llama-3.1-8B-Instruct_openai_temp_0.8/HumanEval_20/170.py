```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of at least two numbers.

    Returns:
    Tuple[float, float]: A tuple of two numbers that are the closest to each other.

    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = None

    # Iterate over all pairs to find the closest one
    for pair in pairs:
        # Calculate the absolute difference between the two numbers in the pair
        diff = abs(pair[0] - pair[1])
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair

    # Return the closest pair in order (smaller number, larger number)
    return tuple(sorted(closest_pair))
```

This script uses the `itertools.combinations` function to generate all possible pairs of numbers in the list. It then iterates over these pairs to find the pair with the smallest absolute difference, which represents the two numbers that are closest to each other. The `sorted` function is used to ensure that the numbers in the closest pair are returned in order (smaller number, larger number).