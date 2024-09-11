### Find Closest Elements
#### A Python Script to Find Two Closest Elements in a List
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find and return two elements in a list that are the closest to each other.
    
    Args:
    numbers (List[float]): A list of numbers with at least two elements.
    
    Returns:
    Tuple[float, float]: A tuple containing the two closest elements in ascending order.
    """
    # First, sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()
    
    # Iterate over the sorted list to find the closest pair of numbers
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        
        # If the difference is less than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    # Return the closest pair of numbers
    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script sorts the input list of numbers in ascending order and then iterates over the sorted list to find the closest pair of numbers by calculating the difference between each pair of adjacent numbers. The pair with the minimum difference is returned. The example usage demonstrates the function with two different lists of numbers.