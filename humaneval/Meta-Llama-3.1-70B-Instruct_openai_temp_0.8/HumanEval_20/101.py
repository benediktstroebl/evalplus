```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each 
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    Tuple[float, float]: A tuple of two numbers that are closest to each other.
    """
    # First, sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()  # Initialize with an empty tuple

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    # Return the closest pair
    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of two numbers that are closest to each other. The function first sorts the list of numbers and then iterates over the sorted list to find the closest pair. The closest pair is updated whenever a smaller difference is found. The function finally returns the closest pair. The script also includes test cases to verify the correctness of the function.