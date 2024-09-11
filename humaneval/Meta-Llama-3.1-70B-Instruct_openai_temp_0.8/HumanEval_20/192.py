```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair with the first two elements
    min_diff = numbers[1] - numbers[0]
    closest_pair = (numbers[0], numbers[1])

    # Iterate through the sorted list to find the closest pair
    for i in range(1, len(numbers) - 1):
        # Calculate the difference between the current element and the next one
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the closest pair
    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input, sorts the list, and then iterates through the sorted list to find the closest pair of numbers. The function returns the closest pair in order (smaller number, larger number).

The script also includes two test cases to verify that the function works correctly.