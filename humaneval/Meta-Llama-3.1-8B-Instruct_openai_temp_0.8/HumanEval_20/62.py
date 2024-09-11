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

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # If all numbers are the same, return any two identical numbers
    if len(set(numbers)) == 1:
        return (numbers[0], numbers[0])

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize minimum difference and closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list of numbers with their indices
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the current difference is less than the minimum difference found so far, update the minimum difference and the closest pair of numbers
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the closest pair of numbers
    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This Python script defines a function `find_closest_elements` that takes a list of numbers as input and returns the two numbers that are closest to each other. The function first checks if all numbers are the same, in which case it returns any two identical numbers. Then, it sorts the list of numbers in ascending order and iterates over the sorted list with their indices. For each pair of consecutive numbers, it calculates the difference between them and updates the minimum difference and the closest pair of numbers if the current difference is less than the minimum difference found so far. Finally, it returns the closest pair of numbers.