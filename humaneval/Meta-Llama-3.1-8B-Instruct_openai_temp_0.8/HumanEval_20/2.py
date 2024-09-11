```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in the list.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Check if list is empty
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize minimum difference and closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between current number and next number
        diff = numbers[i + 1] - numbers[i]
        
        # If current difference is smaller than minimum difference, update minimum difference and closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script sorts the list of numbers and then iterates over the list to find the closest pair of numbers. The minimum difference and the closest pair are updated whenever a smaller difference is found. The function raises a ValueError if the list contains less than two numbers.