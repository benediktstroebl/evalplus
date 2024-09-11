```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of at least two floating point numbers.

    Returns:
        A tuple of two floating point numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the sorted list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
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

This script uses a simple iterative approach to find the closest pair of numbers in the sorted list. It initializes the minimum difference and the closest pair of numbers and then iterates over the sorted list to find the pair with the smallest difference. The time complexity of this approach is O(n), where n is the length of the list, since we only need to iterate over the list once.