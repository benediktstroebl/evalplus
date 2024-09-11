```markdown
**Find Closest Elements in a List**
=====================================

This script solves the problem of finding two numbers in a list that are the closest to each other.

**Code**
--------

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple of two floating point numbers that are the closest to each other.

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the pair of closest numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

**Explanation**
---------------

This script defines a function `find_closest_elements` that takes a list of floating point numbers as input. It first checks if the list has at least two elements. If not, it raises a `ValueError`.

It then sorts the list of numbers in ascending order. The initial minimum difference is set to infinity, and the pair of closest numbers is initialized to the first two elements of the list.

The script then iterates over the sorted list, calculating the difference between each pair of adjacent numbers. If the difference is less than the current minimum difference, it updates the minimum difference and the pair of closest numbers.

Finally, the script returns the pair of closest numbers. The test cases demonstrate the function's behavior with different input lists.