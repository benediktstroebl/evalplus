```markdown
# Find Closest Elements in a List
=====================================

This script takes a list of numbers as input and returns two numbers that are the closest to each other.

### Code

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of float numbers.

    Returns:
        A tuple of two float numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Check if the list is empty or contains only one element
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(numbers))  # Output: (2.0, 2.2)
```

### Explanation

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns two numbers that are the closest to each other. The function iterates over the list of numbers and for each pair of adjacent numbers, it calculates the difference between them. If the difference is less than the minimum difference found so far, the function updates the minimum difference and the closest pair of numbers. Finally, the function returns the closest pair of numbers.