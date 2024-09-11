```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers: A list of float numbers of length at least two.

    Returns:
    A tuple of two float numbers that are the closest to each other.

    Example:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))
    
    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')
    closest_pair = None
    
    # Iterate over all pairs of numbers
    for pair in pairs:
        # Calculate the absolute difference between the two numbers in the pair
        diff = abs(pair[0] - pair[1])
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair
    
    # Return the closest pair of numbers
    return tuple(sorted(closest_pair))


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other. The function uses the `itertools.combinations` function to generate all possible pairs of numbers, calculates the absolute difference between each pair, and keeps track of the pair with the minimum difference. The function returns the closest pair of numbers in sorted order. The script also includes test cases to demonstrate the function's behavior.