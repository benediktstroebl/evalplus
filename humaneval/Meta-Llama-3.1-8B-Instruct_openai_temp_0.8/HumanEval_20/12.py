### Python Script to Find Closest Elements in a List
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other
    and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing two numbers that are the closest to each other.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])

    # Iterate through the list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current and next elements
        diff = abs(numbers[i] - numbers[i + 1])

        # Update the minimum difference and the closest pair if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example use cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```
This script uses a simple sorting approach to find the closest pair of numbers in the list. It iterates through the sorted list to find the minimum difference between consecutive elements and returns the corresponding pair. The time complexity of this solution is O(n log n) due to the sorting step, where n is the length of the input list.