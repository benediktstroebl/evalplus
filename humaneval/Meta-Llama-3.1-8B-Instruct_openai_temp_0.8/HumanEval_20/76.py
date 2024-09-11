### Closest Pair of Elements in a List
```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Calculate the difference between each pair of numbers
    differences = [(pair[0] - pair[1], pair) for pair in pairs]

    # Find the pair with the smallest difference
    closest_pair = min(differences, key=lambda x: abs(x[0]))

    # Return the pair of numbers
    return closest_pair[1]

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script uses the `itertools` module to generate all possible pairs of numbers in the list, then calculates the difference between each pair. It finds the pair with the smallest difference and returns the pair of numbers. If two numbers are identical, it will return that number twice.