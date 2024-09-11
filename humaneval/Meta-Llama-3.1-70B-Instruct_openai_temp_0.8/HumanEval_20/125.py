```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers (at least two) from which to select the closest pair.

    Returns:
        Tuple[float, float]: A tuple containing the closest pair of numbers in ascending order.
    """

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # First, we sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the closest pair with the first two elements in the sorted list
    min_diff = sorted_numbers[1] - sorted_numbers[0]
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    
    # Iterate over the sorted list to find the closest pair
    for i in range(1, len(sorted_numbers) - 1):
        # Calculate the difference between the current element and the next one
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        
        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    # Return the closest pair
    return closest_pair

print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```