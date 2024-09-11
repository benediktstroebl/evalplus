```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in the list.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # First, sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list of numbers to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the current difference is smaller than the minimum difference found so far
        if diff < min_diff:
            # Update the minimum difference and the closest pair of numbers
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the closest pair of numbers
    return closest_pair


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns the two closest numbers in the list. The function first sorts the list of numbers, then iterates over the sorted list to find the pair of numbers with the smallest difference. The function returns the closest pair of numbers as a tuple. The script also includes two test cases to demonstrate the function's behavior.