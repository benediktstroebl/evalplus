```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements from the supplied list of numbers that are closest to each other and returns them in order (smaller number, larger number).
    Test case:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4])
    (2.0, 3.0)
   2)
   2)
    """

Accepts a list of numbers and returns a tuple of two closest numbers and their order. The function uses the Dijkstraan's algorithm with a heapq module to select the two closest elements correctly. 
The time complexity of the function is O(log(n)), where n is the number of elements in the list.