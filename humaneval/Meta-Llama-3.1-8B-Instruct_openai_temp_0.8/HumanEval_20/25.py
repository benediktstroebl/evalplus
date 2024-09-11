Here's a Python script that solves the problem:

```markdown
### Closest Number Pairs Finder

This script finds the two numbers in a list that are closest to each other.

#### Code
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of float numbers.

    Returns:
        Tuple[float, float]: A tuple of two closest numbers in the list.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current pair of numbers
        diff = abs(numbers[i] - numbers[i + 1])

        # Update the minimum difference and the closest pair if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script works by first sorting the list of numbers in ascending order. Then, it iterates over the list to find the closest pair of numbers by keeping track of the minimum difference found so far and updating the closest pair accordingly. Finally, it returns the closest pair of numbers as a tuple.