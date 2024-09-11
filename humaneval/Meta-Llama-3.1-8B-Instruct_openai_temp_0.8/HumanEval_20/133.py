```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other
    and return them in order (smaller number, larger number).

    Args:
        numbers: A list of float numbers.

    Returns:
        A tuple of two float numbers which are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Initialize minimum difference and pair
    min_diff = float('inf')
    closest_pair = None

    # Iterate over all pairs to find the one with the minimum difference
    for pair in pairs:
        diff = abs(pair[0] - pair[1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair

    return tuple(sorted(closest_pair))

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(numbers))

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
print(find_closest_elements(numbers))
```
This script uses the `itertools.combinations` function to generate all possible pairs of numbers from the input list. It then iterates over these pairs to find the one with the minimum difference, which is the pair of numbers that are the closest to each other. The `sorted` function is used to ensure that the pair is returned in order (smaller number, larger number).