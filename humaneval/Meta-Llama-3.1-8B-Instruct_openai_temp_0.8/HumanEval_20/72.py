### Find Closest Elements
#### Problem Description
From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of at least two unique float numbers.

    Returns:
        Tuple[float, float]: Two numbers from the input list that are closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list in ascending order
    numbers.sort()

    # Initialize minimum difference and corresponding elements
    min_diff = float('inf')
    closest_elements = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the closest elements
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current and next element
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the current minimum difference, update the minimum difference and closest elements
        if diff < min_diff:
            min_diff = diff
            closest_elements = (numbers[i], numbers[i + 1])

    return closest_elements

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script uses a simple and efficient approach to find the closest elements in the list. It first sorts the list in ascending order and then iterates over it to find the closest elements by calculating the difference between adjacent elements. The closest elements are updated whenever a smaller difference is found. Finally, the function returns the two closest elements in the correct order (smaller number, larger number).