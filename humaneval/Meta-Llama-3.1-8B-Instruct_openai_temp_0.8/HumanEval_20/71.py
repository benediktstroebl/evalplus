```markdown
### Closest Elements Finder
#### A Python Script to Find Two Closest Elements in a List

A script that takes a list of floating point numbers as input and returns two numbers that are closest to each other.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current pair of numbers
        diff = numbers[i + 1] - numbers[i]

        # If the current difference is less than the minimum difference, update the closest pair and the minimum difference
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(numbers))  # Output: (2.0, 2.2)

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
print(find_closest_elements(numbers))  # Output: (2.0, 2.0)
```

This script first checks if the input list has at least two elements. If not, it raises a ValueError. It then sorts the list of numbers in ascending order. The script iterates over the list to find the closest pair of numbers, keeping track of the minimum difference and the closest pair. Finally, it returns the closest pair of numbers.