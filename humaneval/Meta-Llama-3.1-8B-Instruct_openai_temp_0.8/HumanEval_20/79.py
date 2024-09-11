```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of float numbers.

    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in order.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = ()
    
    # Iterate through the sorted list to find the closest pair of numbers
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        
        # If the current difference is smaller than the minimum difference found so far
        if diff < min_diff:
            # Update the minimum difference and the closest pair of numbers
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    # Return the closest pair of numbers
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of float numbers as input, sorts the list in ascending order, and then iterates through the sorted list to find the closest pair of numbers. It returns a tuple containing the two closest numbers in order. The script also includes two test cases to demonstrate the function's behavior.