```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function with known good inputs and known bad inputs
values_good = [5, 3, 'three', (])
values_bad = [1, 'two', (), [1, 2], ['abc']]

assert filter_integers(values_good) == [5, 3, 'three']
assert filter_integers(values_bad) == []
``` 
The function `filter_integers` takes a list of values and returns a new list that contains only the integer values from the original list. It uses the filter function to accomplish this, which is a built-in function in Python. It tests to ensure the filter only elements that are instances of int, and it returns a list of those values.