```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floats with at least two elements.

    Returns:
        Tuple[float, float]: A tuple of two numbers from the input list that are the closest to each other.
    """
    
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()
    
    # Iterate through the list of numbers to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the pair of closest numbers
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of floats as input, sorts the list, and then finds the pair of numbers with the minimum difference. The function returns this pair of numbers as a tuple. The script also includes test cases to demonstrate the function's correctness.