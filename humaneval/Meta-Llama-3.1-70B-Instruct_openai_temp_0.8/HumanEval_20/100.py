```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    Args:
        numbers: A list of float numbers.
    
    Returns:
        A tuple of two float numbers that are the closest to each other in the list.
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')
    closest_pair = ()
    
    # Iterate over the sorted list to find the pair of numbers with the minimum difference
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the pair of numbers with the minimum difference
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```