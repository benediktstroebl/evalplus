### Closest Elements Finder
#### Problem: Find the two closest numbers in a list

Here is a Python script that uses a simple sorting approach to find the closest two numbers in a list:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    Args:
        numbers (List[float]): A list of float numbers.
    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers.
    """
    
    # First, sort the list in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current and next numbers
        diff = numbers[i + 1] - numbers[i]
        
        # If the current difference is smaller than the minimum difference, update it
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script works by first sorting the input list in ascending order. Then, it iterates over the sorted list to find the closest pair of numbers by keeping track of the minimum difference found so far and updating the closest pair whenever a smaller difference is encountered.