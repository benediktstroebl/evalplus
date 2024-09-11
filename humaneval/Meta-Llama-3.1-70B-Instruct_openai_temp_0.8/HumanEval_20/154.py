```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other
    and return them in order (smaller number, larger number).

    Args:
        numbers: A list of floating point numbers.

    Returns:
        A tuple containing the two closest numbers in ascending order.
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")

    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()

    # Iterate over the sorted list of numbers to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```

This script first checks if the input list contains at least two numbers. If not, it raises a ValueError. Then, it sorts the list of numbers in ascending order. After that, it iterates over the sorted list to find the pair of numbers with the smallest difference. Finally, it returns the pair of closest numbers in ascending order. The test cases at the end of the script demonstrate its usage.