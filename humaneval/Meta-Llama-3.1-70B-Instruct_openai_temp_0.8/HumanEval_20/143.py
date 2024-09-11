```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of floating point numbers.

    Returns:
        A tuple of two numbers that are closest to each other in the input list.

    Raises:
        ValueError: If the input list contains less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    # First, we sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()

    # Iterate over the sorted list of numbers to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```