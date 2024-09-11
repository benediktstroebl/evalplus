```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each 
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    Tuple[float, float]: A tuple of two numbers that are the closest to each other in the list.

    Raises:
    ValueError: If the list contains less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = ()

    # Iterate through the sorted list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)

# Edge case test
try:
    print(find_closest_elements([1.0]))
except ValueError as e:
    print(e)  # The list must contain at least two elements.
```