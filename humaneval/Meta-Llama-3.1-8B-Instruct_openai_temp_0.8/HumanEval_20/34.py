### Find Two Closest Elements in a List

This Python script solves the problem of finding two elements in a list of numbers that are the closest to each other.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two elements in the list that are the closest to each other.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    Tuple[float, float]: A tuple containing two numbers that are the closest to each other.

    Raises:
    ValueError: If the list has less than two elements.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current pair
        diff = abs(numbers[i + 1] - numbers[i])

        # Update the minimum difference and the closest pair if necessary
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input, sorts the list, and then iterates over the list to find the closest pair. The function returns the closest pair of numbers. The example usage demonstrates how to use this function with different input lists.