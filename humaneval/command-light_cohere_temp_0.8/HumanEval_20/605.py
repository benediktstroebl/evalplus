```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects two elements that are the closest to each other and returns them in order (smaller number, larger number).
    The function takes a list of numbers as input and returns a tuple of the two closest elements in the list, along with the distance between them.
    """
Return values: 
    - The first element in the tuple (smallest number). 
    - The second element in the tuple (largest number). 
    - The distance between the two elements in the list.
``` 
This function uses the supplied list of numbers and then sorts them based on their values. After that, it returns two values that are the closest to each other and returns them in order.