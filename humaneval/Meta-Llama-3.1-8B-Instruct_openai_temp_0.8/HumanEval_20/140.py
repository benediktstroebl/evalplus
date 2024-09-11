### Find Closest Element Pairs
#### Python Script

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: A tuple of the two closest numbers.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    numbers.sort()  # Sort the list of numbers
    min_diff = float('inf')  # Initialize the minimum difference
    closest_pair = ()  # Initialize the closest pair

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # Calculate the difference between two adjacent numbers

        if diff < min_diff:  # If the difference is smaller than the current minimum difference
            min_diff = diff  # Update the minimum difference
            closest_pair = (numbers[i], numbers[i + 1])  # Update the closest pair

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script sorts the list of numbers and then iterates through the sorted list to find the two numbers that are closest to each other. It keeps track of the minimum difference and the closest pair found so far.