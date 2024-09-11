```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of at least two numbers.

    Returns:
        Tuple[float, float]: A tuple of two numbers that are the closest to each other.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the sorted list of numbers to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current pair of numbers
        diff = abs(numbers[i] - numbers[i + 1])
        
        # If the current difference is less than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the closest pair of numbers
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other. The function first sorts the list of numbers in ascending order, then iterates over the sorted list to find the closest pair of numbers. The function keeps track of the minimum difference and the closest pair of numbers as it iterates over the list. Finally, the function returns the closest pair of numbers. The script includes two test cases to demonstrate the function's behavior.