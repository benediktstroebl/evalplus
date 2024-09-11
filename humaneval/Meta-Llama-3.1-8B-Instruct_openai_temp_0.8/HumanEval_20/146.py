Here's a self-contained Python script that solves the problem:

```markdown
### Find the Closest Pair of Numbers

#### Problem Description

From a supplied list of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).

#### Code

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the closest pair of numbers in a list.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: A tuple containing the closest pair of numbers.
    """
    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current pair
        diff = numbers[i + 1] - numbers[i]

        # Update the minimum difference and the closest pair if necessary
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

#### Output

```
(2.0, 2.2)
(2.0, 2.0)
```

This script sorts the input list of numbers and then iterates over the sorted list to find the closest pair of numbers. The minimum difference between consecutive numbers is used to determine the closest pair.