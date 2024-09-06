```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two numbers that are the closest to each other and returns them in order (smaller number, larger number).
    
    Parameters: 
    - numbers (List[float]) - List of floating-point numbers, at least length two
    Returns: 
    - Tuple[float, float] - Tuple containing the two closest numbers and their order

test_find_closest_elements( [(1.0, 3.0), (2.0, 2.0), (5.0,2.2)])
test_find_closest_elements([1.0, 2.0, 3.0, 4.0, 2])
   test_find_closest_elements([1.0, 2.0, 3.0, 4.0, 2]) # (1.0, 2.0)
test_find_closest_elements([2.0, 3.0, 4.2])
test_find_closest_elements( [(1.0, 2.0), (2.0,3.0), (4.0,2)])
```