```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: A tuple of two numbers that are closest to each other in the list.
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    numbers.sort()  # Sort the list in ascending order

    min_diff = float('inf')  # Initialize minimum difference as infinity
    closest_pair = ()  # Initialize the closest pair as an empty tuple

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # Calculate the difference between two adjacent numbers
        if diff < min_diff:  # If the difference is smaller than the current minimum difference
            min_diff = diff  # Update the minimum difference
            closest_pair = (numbers[i], numbers[i + 1])  # Update the closest pair

    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```