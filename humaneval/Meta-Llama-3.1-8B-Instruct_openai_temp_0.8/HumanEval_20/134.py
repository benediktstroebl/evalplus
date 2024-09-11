### Closest Pair of Numbers
#### Problem
Find the two numbers in a list that are closest to each other and return them in order.

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of float numbers with at least two elements.

    Returns:
    Tuple[float, float]: A tuple of two numbers that are closest to each other.
    """
    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the smallest number

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current and next numbers
        diff = numbers[i + 1] - numbers[i]

        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input, sorts the list, and then iterates over the sorted list to find the pair of numbers with the smallest difference. The function returns a tuple of these two numbers. The test cases demonstrate the function's behavior with different inputs.