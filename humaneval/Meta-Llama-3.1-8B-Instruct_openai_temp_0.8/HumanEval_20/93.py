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
        Tuple[float, float]: A tuple of two floats that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Calculate the difference between each pair
    differences = [(abs(pair[0] - pair[1])) for pair in pairs]

    # Find the index of the pair with the smallest difference
    min_diff_index = differences.index(min(differences))

    # Return the pair with the smallest difference
    return pairs[min_diff_index]

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script uses the `itertools.combinations` function to generate all possible pairs of numbers in the list. It then calculates the absolute difference between each pair and finds the pair with the smallest difference. The pair is then returned as a tuple. If two numbers in the list are equal, the function will return them both as the closest pair.