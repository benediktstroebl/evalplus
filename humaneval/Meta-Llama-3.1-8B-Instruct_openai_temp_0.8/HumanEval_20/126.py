### Closest Pair of Numbers in a List
```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other
    and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in the list.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Combine the list with itself, shifted by one element, to get all possible pairs
    pairs = list(itertools.combinations(numbers, 2))
    
    # Calculate the absolute difference between each pair
    differences = [abs(pair[0] - pair[1]) for pair in pairs]
    
    # Find the minimum difference and the pair that achieves it
    min_diff = min(differences)
    closest_pair = next(pair for pair, diff in zip(pairs, differences) if diff == min_diff)
    
    return tuple(sorted(closest_pair))
```

This script defines a function `find_closest_elements` that takes a list of floating point numbers as input and returns a tuple containing the two numbers that are closest to each other. The function uses the `itertools.combinations` function to generate all possible pairs of numbers, calculates the absolute difference between each pair, and then finds the pair with the minimum difference. The function returns this pair as a tuple, sorted in ascending order.

The example usage is also provided in the docstring, demonstrating how to use the function to find the closest pair of numbers in a given list.