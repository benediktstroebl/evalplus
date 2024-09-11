```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of floats

    Returns:
        A tuple of two floats, the closest to each other in the list, in ascending order.
    """
    # Check if list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()

    # Iterate through the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example use cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest numbers in the list, in ascending order. The function first sorts the list of numbers, then iterates through the sorted list to find the closest pair by calculating the difference between each pair of adjacent numbers and updating the minimum difference and the closest pair as needed.