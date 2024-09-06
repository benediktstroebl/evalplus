```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # sort the list of numbers
    numbers.sort(numbers, key=lambda x: x)
    # remove the last element
    numbers.remove(numbers[-1])
    # get the first two elements from the sorted list
    first, second = numbers[:2]
    return first, second
```
This script defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements in the list. The function first sorts the by elements and then removes the last element to get the two desired elements.