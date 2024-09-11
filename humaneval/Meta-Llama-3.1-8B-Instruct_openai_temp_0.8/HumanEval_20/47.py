```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of floating point numbers of length at least 2.

    Returns:
    Tuple[float, float]: A tuple containing two closest numbers to each other in the list.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Generate all possible pairs of numbers from the list
    pairs = list(itertools.combinations(numbers, 2))
    
    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = None
    
    # Iterate over all pairs to find the closest pair
    for pair in pairs:
        diff = abs(pair[0] - pair[1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair
    
    return tuple(sorted(closest_pair))

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script uses the `itertools.combinations` function to generate all possible pairs of numbers from the list. It then iterates over these pairs to find the one with the smallest difference between the two numbers. The `sorted` function is used to ensure the pair is returned in the correct order (smaller number, larger number).