Here is the solution:
```python
from typing import List
from math import sqrt

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number). 
    The algorithm used is the Euclidean distance, which calculates the straight-line distance between two points.
    """ Return the area: The first element is the smallest distance.
    return: A tuple containing the first element that is the smallest distance from the second element.
    """

def test_find_closest_elements():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    first_closest_elements = find_closest_elements(numbers)
    assert (first_element == (2.0, 3.0))  # contains two elements that are the closest to each other

```
The test function test_find_closest_elements is a simple Python script that creates a list of numbers [1.0, 2.0, 3.0, 4.0, 5.0] and passes the cue to test if the function can solve the problem and return the correct result.