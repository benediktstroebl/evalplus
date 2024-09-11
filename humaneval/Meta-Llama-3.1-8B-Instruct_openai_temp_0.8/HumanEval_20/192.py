### Python Script to Find Two Closer Numbers in a List
```markdown
### Description
This script finds the two closest numbers in a given list of numbers.

### Usage
To use this script, simply call the `find_closest_elements` function and pass in your list of numbers as an argument.

### Code
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    Tuple[float, float]: A tuple of two numbers that are the closest to each other.

    Example:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the pair of numbers with the minimum difference
    return closest_pair
```

### Example Usage
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(numbers))  # Output: (2.0, 2.2)

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
print(find_closest_elements(numbers))  # Output: (2.0, 2.0)
```