```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    This function finds the two closest numbers in a list and returns them in order.
    
    Args:
    numbers (List[float]): A list of floating point numbers with a length of at least two.
    
    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in the list, in order from smallest to largest.
    """
    
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()  # Initialize with an empty tuple
    
    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next number
        diff = abs(numbers[i] - numbers[i + 1])
        
        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the closest pair of numbers
    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```