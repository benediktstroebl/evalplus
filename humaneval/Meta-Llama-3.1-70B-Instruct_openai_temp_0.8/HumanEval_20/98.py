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
        Tuple[float, float]: The two closest numbers.
    """
    # First, we sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = None

    # Generate all possible pairs of adjacent numbers in the sorted list
    for num1, num2 in itertools.pairwise(numbers):
        # Calculate the difference between the two numbers in the pair
        diff = num2 - num1

        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (num1, num2)

    # Return the pair of numbers with the minimum difference
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```