```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    Args:
    numbers: A list of floats (length >= 2)
    
    Returns:
    A tuple of two floats, the closest pair in the list in ascending order
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required")
    
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = ()
    
    # Iterate over the sorted list of numbers to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Example usage
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```