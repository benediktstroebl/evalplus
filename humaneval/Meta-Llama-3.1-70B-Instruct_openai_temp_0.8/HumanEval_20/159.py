```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of floats with a length of at least 2.

    Returns:
        A tuple of two floats representing the closest pair of numbers in the list.

    Raises:
        ValueError: If the input list has less than 2 elements.
    """

    # Check if the input list has at least 2 elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least 2 elements.")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = ()

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)

# Error test case
try:
    print(find_closest_elements([1.0]))
except ValueError as e:
    print(e)  # Input list must have at least 2 elements.
```