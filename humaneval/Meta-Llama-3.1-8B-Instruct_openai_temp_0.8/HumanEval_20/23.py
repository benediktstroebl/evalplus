Here is a Python script that solves the problem.
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of at least two floating point numbers.

    Returns:
        A tuple of two floating point numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # First, we sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference between two numbers, and the pair of numbers with this difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()

    # Iterate over the sorted list of numbers to find the pair with the minimum difference
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = sorted_numbers[i + 1] - sorted_numbers[i]

        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script defines a function `find_closest_elements` that takes a list of floating point numbers as input, sorts the list in ascending order, and then iterates over the sorted list to find the pair of numbers with the minimum difference. The function returns this pair of numbers. The script also includes test cases to demonstrate the function's behavior.