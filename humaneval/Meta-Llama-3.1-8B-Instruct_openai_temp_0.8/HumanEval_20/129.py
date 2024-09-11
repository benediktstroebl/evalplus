```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other 
    and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers with a length of at least two.

    Returns:
        Tuple[float, float]: A tuple containing two numbers that are the closest to each other in the list.

    Raises:
        ValueError: If the input list has less than two elements.
    """
    
    # Check if the list has less than two elements and raise a ValueError if true
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")
    
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        
        # If the current difference is less than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other in the list. The function first checks if the list has less than two elements and raises a `ValueError` if true. Then it sorts the list of numbers and initializes the minimum difference and the closest pair of numbers. It iterates over the list to find the closest pair of numbers and returns them as a tuple. The script also includes test cases to demonstrate the function's behavior.