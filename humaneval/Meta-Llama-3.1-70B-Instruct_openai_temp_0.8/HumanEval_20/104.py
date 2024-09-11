Here's a Python script that solves the problem using a simple, yet efficient approach. This script sorts the list of numbers and then iterates over the sorted list to find the closest pair.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    :param numbers: A list of numbers
    :return: A tuple of the closest two numbers
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers")

    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (None, None)

    # Iterate over the sorted list to find the closest pair
    for i in range(1, len(sorted_numbers)):
        diff = sorted_numbers[i] - sorted_numbers[i - 1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i - 1], sorted_numbers[i])

    return closest_pair


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```

This script first checks if the list contains at least two numbers. It then sorts the list and initializes the minimum difference and the closest pair. It iterates over the sorted list, calculates the difference between each pair of numbers, and updates the minimum difference and the closest pair if a smaller difference is found. Finally, it returns the closest pair of numbers.