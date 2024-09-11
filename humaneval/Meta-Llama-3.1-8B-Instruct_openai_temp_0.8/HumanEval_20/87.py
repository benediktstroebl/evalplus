```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers with at least two elements.

    Returns:
    Tuple[float, float]: A tuple containing two numbers that are the closest to each other.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Find the pair with the smallest difference
    closest_pair = min(pairs, key=lambda x: abs(x[0] - x[1]))

    return closest_pair
```

This script uses the `itertools.combinations` function to generate all possible pairs of numbers from the input list. It then uses the built-in `min` function with a custom key function to find the pair with the smallest difference, which are the two numbers that are closest to each other. If there are multiple pairs with the same smallest difference, the script will return the first one it encounters.