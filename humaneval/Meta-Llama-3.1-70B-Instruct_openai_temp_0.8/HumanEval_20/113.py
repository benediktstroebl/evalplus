```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating-point numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers.
    """

    # Check if the list has less than two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = None

    # Iterate over the list to find the closest pair
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference between the current pair of numbers
            diff = abs(numbers[i] - numbers[j])

            # If the current difference is less than the minimum difference found so far, update the minimum difference and the closest pair
            if diff < min_diff:
                min_diff = diff
                closest_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

This script defines the function `find_closest_elements` which takes a list of floating-point numbers as input and returns a tuple containing the two closest numbers. The function iterates over the list to find the closest pair by calculating the absolute difference between each pair of numbers and keeping track of the minimum difference found so far. Finally, it returns the pair of numbers with the minimum difference in ascending order.