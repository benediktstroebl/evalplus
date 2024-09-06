```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Use the built-in function and transpose it to sort the list
    return sorted((a, b) for a, b in zip(numbers)), key=lambda t: t[0]*t[1])[::-1]
```
The function sorts the list using the built-in function `sorted()` with the `key` parameter set to a lambda function that returns the product of the two elements of the tuple (a,b) passed in the `zip()` function.  The result function then sorts the elements in ascending order, and returns a tuple of the two closest elements.