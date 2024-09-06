Here's the solution:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two closest elements from the input list """
    # Sort the list
    numbers.sort()
    Then original order of the list
    # Find the first two closest elements and return them
    a, b = numbers[0], numbers[1]
    if a == b:
        return (a, a)
    if a > b:
        return (a, b)
    return (b, a)
```

The function `find_closest_elements` takes a list of numbers and returns a tuple of the two closest elements in the list, in ascending order. The function first sorts the old-fashioned way by sorting the list and then finds the first two closest elements. It then compares the the specific elements to each other, and returns the closest element to the other one as a tuple.