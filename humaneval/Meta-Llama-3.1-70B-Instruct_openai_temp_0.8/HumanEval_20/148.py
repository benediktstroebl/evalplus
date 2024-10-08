```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: A tuple of the two closest numbers.
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])

    # Iterate over the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```
This script first checks if the list has at least two elements. It then sorts the list of numbers and initializes the minimum difference and the closest pair. It iterates over the sorted list to find the closest pair by calculating the difference between each pair of adjacent numbers. If it finds a pair with a smaller difference, it updates the minimum difference and the closest pair. Finally, it returns the closest pair.