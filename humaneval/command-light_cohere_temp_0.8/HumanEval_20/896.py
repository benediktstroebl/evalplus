Here is a Python script that solves the problem you described:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Make sure the list has at least two elements
    if len(numbers) < 2:
        return numbers, None
    
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    # Get the first two elements
    first_element, second_element = sorted_numbers[0:2]
    # Return the two closest elements
    return first_element, second_element
```
This code defines a function called `find_closest_elements` that takes a list of numbers as an argument and returns a tuple of the two closest elements in the list, along with their relative order. 
The function first checks if the list has at least two elements, and if not, returns the list along with `None` to indicate that there is not enough elements to find the closest pair. 
The function then sorts the list in ascending order and extracts the first two elements. Then, it returns the pair of these two elements, which are the closest elements to each other in the sorted list.