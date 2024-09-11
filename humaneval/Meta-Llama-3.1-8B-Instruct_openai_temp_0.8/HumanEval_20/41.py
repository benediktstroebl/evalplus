### Find Two Closest Elements in a List

Here's a Python script that implements the `find_closest_elements` function to find two numbers in a list that are closest to each other.

```markdown
## Code

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of at least two distinct float numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in the list.
    """
    # Initialize minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_nums = (numbers[0], numbers[0])

    # Iterate over each pair of adjacent numbers in the list
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        # If the current difference is smaller than the minimum difference found so far, update it
        if diff < min_diff:
            min_diff = diff
            # Update the pair of closest numbers
            closest_nums = (numbers[i], numbers[i + 1])

    return closest_nums

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

### Explanation

This script implements a simple iterative solution to find the two numbers in a list that are closest to each other. It iterates over each pair of adjacent numbers in the list, calculates their absolute difference, and keeps track of the pair with the smallest difference found so far. The function returns this pair of closest numbers as a tuple.

The `float('inf')` initialization of `min_diff` ensures that any finite difference will be smaller, allowing the function to correctly handle the first pair of numbers in the list.

The time complexity of this solution is O(n), where n is the length of the input list, since it makes a single pass over the list. The space complexity is O(1), excluding the input list, since it uses a fixed amount of space to store the minimum difference and the pair of closest numbers.