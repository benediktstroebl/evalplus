```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: A tuple of two numbers that are closest to each other.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Sort the list of numbers
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


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

This script first checks if the input list has at least two elements. It then sorts the list and iterates over it to find the closest pair of numbers. The closest pair is updated whenever a pair with a smaller difference is found. The function finally returns the closest pair.