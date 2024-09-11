### Closest Pair Finder
Below is a Python script that finds the closest pair of elements in a given list.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the closest pair of elements in a given list.

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
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script works by first sorting the list of numbers. Then it iterates over the sorted list, comparing each number with its adjacent number to find the closest pair. The minimum difference is updated whenever a closer pair is found, and the closest pair is updated accordingly. The script finally returns the closest pair.