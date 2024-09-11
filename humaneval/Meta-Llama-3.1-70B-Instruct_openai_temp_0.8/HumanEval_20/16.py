```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    Args:
        numbers (List[float]): A list of numbers of length at least two.
    
    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in order.
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")
    
    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()  # Initialize with an empty tuple
    
    # Generate all possible pairs of numbers
    for num1, num2 in itertools.combinations(numbers, 2):
        # Calculate the absolute difference between the two numbers
        diff = abs(num1 - num2)
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            # Sort the pair to ensure the smaller number comes first
            closest_pair = tuple(sorted([num1, num2]))
    
    # If there are multiple pairs with the same minimum difference, find the first pair in the sorted list of numbers
    sorted_numbers = sorted(numbers)
    for i in range(len(sorted_numbers) - 1):
        if sorted_numbers[i + 1] - sorted_numbers[i] == min_diff:
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
            break
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```