```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    Args:
        numbers (List[float]): A list of floating point numbers.
    
    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in ascending order.
    
    Raises:
        ValueError: If the input list contains less than two elements.
    """
    
    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must contain at least two elements.")
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = ()
    
    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair


# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```