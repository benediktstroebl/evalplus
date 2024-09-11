### Closest Numbers in a List
#### Problem Statement

From a supplied list of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).

#### Solution

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
        Tuple[float, float]: A tuple containing the two numbers that are closest to each other.

    Raises:
        ValueError: If the list contains less than two elements.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Use the pairwise function from the itertools library to get pairs of adjacent numbers
    pairs = itertools.pairwise(numbers)

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = None

    # Iterate over the pairs to find the one with the minimum difference
    for pair in pairs:
        diff = abs(pair[0] - pair[1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair

    # Return the closest pair
    return tuple(sorted(closest_pair))
```

This script uses the pairwise function from the itertools library to get pairs of adjacent numbers in the list.
It then iterates over these pairs to find the one with the minimum difference, which corresponds to the pair of numbers that are closest to each other. The script returns this pair as a tuple, sorted in ascending order. If the list contains less than two elements, the script raises a ValueError.