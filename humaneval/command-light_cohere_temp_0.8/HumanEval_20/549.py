```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns the two closest values from a list of numbers and their relative order """
    # Sorting the list
    sorted_numbers = sorted(numbers)
    
    # Getting the first two elements from the sorted list
    first_two = sorted_numbers[:2]
    
    # Finding the elements that are closest to each other
    closest = [(x, y) for x, y in zip(first_two, first_two[1:]) if x[0] < y[0] and x[1] < y[1]]]
    
    return closest[0], closest[1]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = (2.0, 2.0)

find_closest_elements(numbers)
```