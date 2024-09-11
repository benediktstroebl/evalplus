```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers with a length of at least two.

    Returns:
        Tuple[float, float]: A tuple containing the two numbers that are the closest to each other.
    """
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the sorted list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the current difference is smaller than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two numbers that are the closest to each other. The function first sorts the list in ascending order, then iterates over the sorted list to find the closest pair of numbers by calculating the difference between each pair of adjacent numbers. The pair with the smallest difference is returned as the result. The script also includes two test cases to demonstrate the function's correctness.