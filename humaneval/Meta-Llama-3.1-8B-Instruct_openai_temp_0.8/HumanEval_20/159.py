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
        Tuple[float, float]: A tuple containing two numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Generate all possible pairs of numbers from the list
    pairs = list(itertools.combinations(numbers, 2))

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')
    closest_pair = None

    # Iterate over all pairs to find the pair with the minimum difference
    for pair in pairs:
        # Calculate the absolute difference between the two numbers in the pair
        diff = abs(pair[1] - pair[0])
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = pair

    # Return the pair of numbers with the minimum difference
    return (*sorted(closest_pair),)

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns the pair of numbers that are the closest to each other. The function uses the `itertools.combinations` function to generate all possible pairs of numbers from the list, and then iterates over these pairs to find the pair with the minimum difference. The function returns the pair of numbers with the minimum difference, sorted in ascending order.

The script also includes two test cases to demonstrate the function's behavior. The first test case shows that the function correctly returns the pair of numbers with the minimum difference when the list contains a pair of numbers that are close to each other but not identical. The second test case shows that the function correctly returns a pair of identical numbers when the list contains a pair of identical numbers.