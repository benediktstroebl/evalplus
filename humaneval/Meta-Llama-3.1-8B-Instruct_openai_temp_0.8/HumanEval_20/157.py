Here is a Python script that implements the `find_closest_elements` function:
```markdown
# Find Closest Elements
=====================================

This script finds the two closest elements in a list of numbers.

### find_closest_elements function
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two numbers in the list that are the closest to each other.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: Two numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = None

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current element and the next element
        diff = numbers[i + 1] - numbers[i]
        # If the difference is less than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair
```

### Example Usage
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
# Output: (2.0, 2.2)

print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
# Output: (2.0, 2.0)
```

Note: This script assumes that the input list contains only unique elements. If the list contains duplicate elements, the script may return multiple pairs of closest elements.