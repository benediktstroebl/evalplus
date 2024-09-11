```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of float numbers

    Returns:
        A tuple of two float numbers that are the closest to each other
    """
    # First, sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[0])
    
    # Iterate through the sorted list to find the pair with the minimum difference
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        
        # If the current difference is smaller than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of float numbers as input and returns a tuple of two float numbers that are the closest to each other. The function first sorts the list of numbers in ascending order, then iterates through the sorted list to find the pair with the minimum difference. The function returns this pair of closest numbers. The test cases demonstrate the function's correctness.