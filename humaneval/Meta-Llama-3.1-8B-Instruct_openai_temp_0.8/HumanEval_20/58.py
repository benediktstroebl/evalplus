```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two numbers closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    numbers.sort()  # Sort the list of numbers
    min_diff = float('inf')  # Initialize the minimum difference as infinity
    closest_pair = ()  # Initialize the closest pair as an empty tuple

    # Iterate over the list of numbers to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # Calculate the difference between the current pair of numbers
        if diff < min_diff:  # If the current difference is less than the minimum difference
            min_diff = diff  # Update the minimum difference
            closest_pair = (numbers[i], numbers[i + 1])  # Update the closest pair

    return closest_pair  # Return the closest pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script first sorts the list of numbers. Then it iterates over the sorted list to find the pair of numbers with the minimum difference. If the current difference is less than the minimum difference, it updates the minimum difference and the closest pair. Finally, it returns the closest pair.