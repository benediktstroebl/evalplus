```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of at least two float numbers.

    Returns:
        Tuple[float, float]: A tuple containing two numbers from the list that are the closest to each other.
    """
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the list of numbers to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = numbers[i + 1] - numbers[i]
        
        # If the current difference is smaller than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script uses a simple sorting approach to find the closest pair of numbers in the list. It first sorts the list of numbers, then iterates over the list to find the pair with the smallest difference. The pair with the smallest difference is considered to be the closest pair of numbers.