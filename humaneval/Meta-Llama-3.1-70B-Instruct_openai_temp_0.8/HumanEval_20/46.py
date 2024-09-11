```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of float numbers with at least two elements.

    Returns:
        A tuple of two float numbers that are the closest to each other.

    Raises:
        ValueError: If the input list has less than two elements.
    """

    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[1])

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # Update the minimum difference and the pair of numbers with the minimum difference if necessary
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```