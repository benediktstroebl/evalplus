```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Selects and returns two elements in the list that are the closest to each other 
    and returns them in order of smaller number, larger number
    :param numbers: List[float] - List of floating-point numbers
    :return: Tuple[float, float] - A tuple containing the two elements in order of smaller number, 
    larger number 
    """
    # Sort the list
    numbers.sort()
   
    ordered_list = sorted(numbers)
    # Get the first two elements in the sorted list
    first = tuple(ordered_list[:2])
    # Get the rest of the list elements
    second = tuple(ordered_list[2:])
    # Return the two elements in the tuple
    return first, second
```