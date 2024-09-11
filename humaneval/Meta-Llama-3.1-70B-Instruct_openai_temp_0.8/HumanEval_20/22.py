```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other 
    and return them in order (smaller number, larger number).

    Args:
        numbers: A list of float numbers

    Returns:
        A tuple of two float numbers that are closest to each other
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()  # Initialize with an empty tuple

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference
        if diff < min_diff:
            # Update the minimum difference and the pair of closest numbers
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the pair of closest numbers
    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```