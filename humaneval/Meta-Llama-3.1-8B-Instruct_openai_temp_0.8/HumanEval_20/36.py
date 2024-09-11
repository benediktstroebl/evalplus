### Find Closest Elements
#### Problem: Find two numbers in a list that are the closest to each other.

```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of float numbers.

    Returns:
        Tuple[float, float]: A tuple of two closest float numbers.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Initialize the minimum difference and the pair with the minimum difference
    min_diff = float('inf')
    closest_pair = None

    # Iterate over all pairs to find the pair with the minimum difference
    for pair in pairs:
        # Calculate the absolute difference between the two numbers in the pair
        diff = abs(pair[0] - pair[1])
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair

    # Return the pair with the minimum difference
    return closest_pair
```

### Example Usage
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```