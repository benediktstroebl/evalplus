```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    Tuple[float, float]: A tuple of two numbers in the list that are closest to each other.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()  # Initialize with an empty tuple

    # Iterate over the sorted list of numbers to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```
This script sorts the list of numbers and then iterates over the sorted list to find the pair of numbers with the minimum difference. It keeps track of the minimum difference and the pair of numbers with the minimum difference, and returns the pair at the end.