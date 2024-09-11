Here is a Python function that solves the problem. This function uses the built-in `sorted` function to sort the numbers and then iterates through the sorted list to find the closest numbers.

```markdown
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
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the closest numbers
    min_diff = float('inf')
    closest_numbers = (sorted_numbers[0], sorted_numbers[0])

    # Iterate through the sorted list to find the closest numbers
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_numbers = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_numbers

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This function works by first sorting the list of numbers. Then it iterates through the sorted list, keeping track of the minimum difference between two adjacent numbers and the closest numbers. Finally, it returns the closest numbers. If there are multiple pairs of numbers with the same minimum difference, this function will return the first pair it finds.

This function has a time complexity of O(n log n) due to the sorting step, where n is the number of numbers in the list. The subsequent iteration step has a time complexity of O(n), but it does not dominate the sorting step.