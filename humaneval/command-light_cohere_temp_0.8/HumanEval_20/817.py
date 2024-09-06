Here's a Python script that implements the function `find_closest_elements` to find the two closest elements in a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns the two closest elements in the list, in order of their values.
    """return tuple(sorted((x[0] < y[0] and x[1] < y[1]) for x, y in zip(numbers)))[0, 1])
```
This function employs the sorted() function and a nested loop to compare pairs of elements in the list, selecting the two that are the closest to each other. It returns a more descriptive output than just a tuple, which should make it easier to understand.