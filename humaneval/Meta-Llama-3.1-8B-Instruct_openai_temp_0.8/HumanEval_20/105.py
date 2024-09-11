```python
from typing import List, Tuple

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

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference between two numbers and the pair of numbers with this difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (None, None)

    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next one
        diff = abs(numbers[i] - numbers[i + 1])

        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script defines a function `find_closest_elements` that takes a list of floating point numbers as input and returns a tuple containing the two closest numbers in the list. The function first sorts the list in ascending order, then iterates over the sorted list to find the pair of numbers with the minimum difference. This is done by iterating over the list and calculating the absolute difference between each pair of adjacent numbers. If the current difference is smaller than the minimum difference found so far, the minimum difference and the closest pair are updated. Finally, the function returns the closest pair of numbers.