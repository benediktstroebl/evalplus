```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple of two numbers that are the closest to each other.
    """
    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()

    # Iterate through the list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current pair
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the minimum difference found so far, update it
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of floating point numbers, sorts it, and then iterates through the list to find the pair with the minimum difference. It returns this closest pair as a tuple. The test cases at the end demonstrate the function's behavior.