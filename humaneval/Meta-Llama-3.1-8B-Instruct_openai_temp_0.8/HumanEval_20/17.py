```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing two numbers that are the closest to each other in the list.
    """

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_nums = (numbers[0], numbers[0])  # Initialize with the first two numbers

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next number
        diff = abs(numbers[i] - numbers[i + 1])

        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest numbers
        if diff < min_diff:
            min_diff = diff
            closest_nums = (numbers[i], numbers[i + 1])

    # Return the closest numbers
    return closest_nums

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of floating point numbers as input and returns a tuple containing two numbers that are the closest to each other in the list. The function first sorts the list of numbers, then iterates over the sorted list to find the minimum difference between adjacent numbers. The two numbers with the minimum difference are returned as a tuple. The script includes two test cases to demonstrate the function's behavior.