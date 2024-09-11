```markdown
### Problem: Find Two Closest Numbers in a List

#### Solution: Python Script

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of at least two numbers.

    Returns:
        Tuple[float, float]: A tuple of two numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over all pairs of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference between the current pair of numbers
            diff = abs(numbers[j] - numbers[i])

            # If the current difference is smaller than the minimum difference, update the minimum difference and the closest pair
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

#### Explanation

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other.

The function iterates over all pairs of numbers in the list, calculates the absolute difference between each pair, and keeps track of the pair with the smallest difference.

The time complexity of this solution is O(n^2), where n is the length of the input list, because it involves iterating over all pairs of numbers.

The space complexity is O(1), because it only uses a constant amount of space to store the minimum difference and the closest pair of numbers.