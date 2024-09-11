```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers of length at least two.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in order.
    """
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next one
        diff = abs(numbers[i] - numbers[i + 1])
        
        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script sorts the list of numbers and then iterates over the sorted list to find the pair with the minimum difference. The minimum difference and the closest pair are updated whenever a smaller difference is found. The function finally returns the pair of closest numbers. The test cases are included at the end of the script to verify that the function works as expected.