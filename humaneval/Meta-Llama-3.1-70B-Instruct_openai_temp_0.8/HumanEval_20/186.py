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
    
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Sort the list of numbers
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = ()
    
    # Iterate through the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next number
        diff = abs(numbers[i] - numbers[i + 1])
        
        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```