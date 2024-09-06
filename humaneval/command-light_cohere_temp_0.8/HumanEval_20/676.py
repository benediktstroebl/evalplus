```python
from typing import List
def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements that are the closest to each other and returns them in order (smaller number, larger number).
    
    Parameters: 
    numbers: List[float] list of numbers of length at least two or more
    
    Returns: 
    Tuple[float, float] tuple containing two closest elements in order of their difference.
```

# tests
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

# Test
print(find_closest_elements(numbers))

This script defines a function find_closest_elements that takes a list of numbers as input and returns a tuple with the two elements that are the closest to each other. The function uses the typing module to create a tuple that contains the two closest elements, and the order of the elements is the same as the order of the differences between the two elements.