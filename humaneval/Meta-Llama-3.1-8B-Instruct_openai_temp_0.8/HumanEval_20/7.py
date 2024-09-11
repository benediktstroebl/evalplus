### Closest Elements Finder

This script finds the two closest elements in a list of numbers.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    Tuple[float, float]: A tuple of two floating point numbers that are the closest to each other.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the first pair of numbers

    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test the function with some examples
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other. The function sorts the list of numbers in ascending order, then iterates over the sorted list to find the pair of numbers with the minimum difference. The function uses a sliding window approach to calculate the difference between each pair of adjacent numbers, which allows it to efficiently find the pair with the minimum difference.