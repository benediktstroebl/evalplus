### find_closest_elements Function
### =================================

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers.

    Example:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and closest pair variables
    min_diff = float('inf')
    closest_pair = ()
    
    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next number
        diff = abs(numbers[i] - numbers[i + 1])
        
        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the closest pair
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])) 
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

In this script, the `find_closest_elements` function takes a list of floating point numbers as input, sorts it in ascending order, and then iterates over the sorted list to find the closest pair of numbers. The `abs` function is used to calculate the absolute difference between each pair of numbers. The function keeps track of the minimum difference and the closest pair found so far and returns the closest pair at the end.

The script also includes two test cases to demonstrate the functionality of the `find_closest_elements` function.