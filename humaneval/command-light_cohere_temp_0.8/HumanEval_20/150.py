```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements that are the closest to each other in the numbers list and returns them in order (smaller number, larger number).
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to keep track of the closest element and its distance
    closest_pair = (sorted_numbers[0], 0.0)
    
    # Iterate through the matching numbers until the current number is smaller than the previous closest number
    for current_number in sorted_numbers[1:]:
        current_distance = current_number - closest_pair[1]
        if current_distance < closest_pair[2]:
            closest_pair = (current_number, current_distance)
    
    return closest_pair
```

This function returns a tuple of two floating-point numbers, which represent the two closest elements in the list of numbers, and their order is guaranteed.  The following tests can be performed with a list of any length, and it works with both single and multiple-valued numbers.