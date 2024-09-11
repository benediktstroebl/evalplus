```markdown
### Find Closest Elements in a List

This Python script takes a list of numbers as input and returns the two closest numbers in the list.

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
        Tuple[float, float]: A tuple containing the two closest numbers in the list.
    """
    # Generate all possible pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))
    
    # Initialize the minimum difference and the corresponding pair of numbers
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
    
    # Return the closest pair of numbers in order (smaller number, larger number)
    return tuple(sorted(closest_pair))

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script first generates all possible pairs of numbers in the list using the `itertools.combinations` function. Then, it iterates over all pairs, calculates the absolute difference between the two numbers in each pair, and updates the minimum difference and the closest pair if a smaller difference is found. Finally, it returns the closest pair of numbers in order (smaller number, larger number).