```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in order.
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers")

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the two closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
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
```