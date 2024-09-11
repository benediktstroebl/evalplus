```markdown
### Script: Find Two Closest Numbers in a List

This Python script defines a function `find_closest_elements` that takes a list of numbers as input and returns two numbers that are closest to each other.

#### Code
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two numbers in the list that are the closest to each other.

    Args:
        numbers: A list of numbers with at least two elements.

    Returns:
        A tuple containing two numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # Update the minimum difference and the pair of closest numbers if necessary
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
#### Explanation

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns two numbers that are closest to each other.

1. The list of numbers is first sorted in ascending order.
2. The function then iterates over the sorted list to find the pair of numbers with the minimum difference.
3. The minimum difference and the pair of closest numbers are updated whenever a smaller difference is found.
4. Finally, the function returns the pair of closest numbers.

The example usage demonstrates how to use the `find_closest_elements` function to find the two closest numbers in a list.