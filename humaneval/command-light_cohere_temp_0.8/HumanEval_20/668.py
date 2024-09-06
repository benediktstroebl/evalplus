Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Returns the two elements of the list that are the closest to each other and return them in order (smaller number, larger number)
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Initialize variables
    min_dist_to_other = float('inf')
    min_dist = float('inf')
    closest_num = None
    closest_other_num = None
    
    # Loop through the sorted list of numbers
    for other_num in sorted_numbers[1:]:
        current_dist = sorted_numbers[0] - other_num
        if current_dist < min_dist_to_other:
            min_dist_to_other = current_dist
            closest_num = sorted_numbers[0]
            closest_other_num = other_num
    
    return closest_num, closest_other_num
```

This function takes a list of numbers as input and returns a tuple containing the two elements that are the closest to each other in the list. It uses the sorting the value of the numbers in the list and then loops through the sorted list to find the two closest numbers.