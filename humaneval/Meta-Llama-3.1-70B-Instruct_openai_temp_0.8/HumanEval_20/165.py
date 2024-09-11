```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of floating-point numbers.

    Returns:
        A tuple containing the two closest numbers in the list.
    """
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()  # Initialize with an empty tuple

    # Sort the list of numbers
    numbers.sort()

    # Iterate through the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

This script defines the `find_closest_elements` function, which takes a list of floating-point numbers as input and returns the pair of numbers that are closest to each other. The function first checks if the input list has at least two elements and raises a `ValueError` if not. It then sorts the list of numbers and iterates through the sorted list to find the closest pair. The function returns the closest pair as a tuple, with the smaller number first.