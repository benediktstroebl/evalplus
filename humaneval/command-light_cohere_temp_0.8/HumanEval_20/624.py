```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ 
    Return the elements that are the two closest numbers and return them in order, smallest to largest.
    """
    first, second: 
        = sorted([(num, dist) for (num, dist) in zip(numbers, numbers[::-1])], key=lambda x: x[1])
        return first, second
```
The code defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest numbers. The function first sorts the priority the elements in the list and then returns the first two elements that were sorted, which are the two closest numbers.

The function's test case can be used to check if it is working correctly.