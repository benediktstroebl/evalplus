```markdown
### Closest Elements Finder

This script finds two elements in a list that are closest to each other.

#### Code

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    Tuple[float, float]: Two numbers in the list that are the closest to each other.

    Example:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Create a copy of the input list to avoid modifying the original list
    numbers_copy = numbers.copy()

    # Sort the copied list in ascending order
    numbers_copy.sort()

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize min_diff as infinity
    closest_pair = (numbers_copy[0], numbers_copy[0])  # Initialize closest_pair with the smallest number twice

    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers_copy) - 1):
        diff = numbers_copy[i + 1] - numbers_copy[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers_copy[i], numbers_copy[i + 1])

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
#### Explanation

This script works by first sorting the input list in ascending order. It then iterates over the sorted list, comparing each pair of adjacent numbers. The pair with the minimum difference is updated whenever a smaller difference is found. The function returns the pair of numbers with the minimum difference. If there are multiple pairs with the same minimum difference, any of them can be returned.