```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers (of length at least two)

    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in order
    """

    # First, sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (sorted_numbers[0], sorted_numbers[1])  # Initialize with the first two numbers

    # Iterate through the sorted list to find the closest pair
    for i in range(1, len(sorted_numbers)):
        diff = sorted_numbers[i] - sorted_numbers[i - 1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i - 1], sorted_numbers[i])

    return closest_pair

# Example usage
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```