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
        Tuple[float, float]: A tuple containing the two closest numbers in the list.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = None
    
    # Generate all possible pairs of numbers
    for pair in itertools.combinations(sorted_numbers, 2):
        # Calculate the absolute difference between the pair of numbers
        diff = abs(pair[0] - pair[1])
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair
    
    return closest_pair


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script first sorts the list of numbers. Then it generates all possible pairs of numbers using the `itertools.combinations` function. For each pair, it calculates the absolute difference between the two numbers. If the difference is smaller than the current minimum difference, it updates the minimum difference and the closest pair. Finally, it returns the closest pair of numbers.