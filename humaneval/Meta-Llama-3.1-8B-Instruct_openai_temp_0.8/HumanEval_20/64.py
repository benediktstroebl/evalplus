Here's a Python script that solves the problem.

```markdown
### Find Two Closest Numbers in a List
#### Problem Description
From a supplied list of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two numbers in the list that are closest to each other.

    Args:
        numbers (List[float]): A list of at least two numbers.

    Returns:
        Tuple[float, float]: Two numbers that are closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the first number

    # Iterate over the list of numbers
    for i in range(len(numbers)):
        # Iterate over the rest of the list of numbers
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference between the current pair of numbers
            diff = abs(numbers[i] - numbers[j])

            # If the current difference is smaller than the minimum difference found so far,
            # update the minimum difference and the pair of numbers with the minimum difference
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    return closest_pair

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(numbers))  # Output: (2.0, 2.2)

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
print(find_closest_elements(numbers))  # Output: (2.0, 2.0)
```

This script uses a brute-force approach to find two numbers in the list that are closest to each other. It iterates over all pairs of numbers in the list, calculates the absolute difference between each pair, and updates the minimum difference and the pair of numbers with the minimum difference as it finds smaller differences. The script also includes example usage to demonstrate how to use the `find_closest_elements` function.