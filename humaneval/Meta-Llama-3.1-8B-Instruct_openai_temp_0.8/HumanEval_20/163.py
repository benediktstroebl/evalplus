```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of floating point numbers with a length of at least two.

    Returns:
        A tuple of two floating point numbers that are the closest to each other in the input list.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # First, we sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (sorted_numbers[0], sorted_numbers[0])
    
    # Iterate over the sorted list to find the closest pair of numbers
    for i in range(1, len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        
        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    # Return the closest pair of numbers
    return closest_pair

# Test the function with the provided examples
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script uses the built-in `sorted` function to sort the list of numbers, and then iterates over the sorted list to find the closest pair of numbers. It keeps track of the minimum difference found so far and updates it whenever it finds a pair of numbers with a smaller difference. Finally, it returns the closest pair of numbers.