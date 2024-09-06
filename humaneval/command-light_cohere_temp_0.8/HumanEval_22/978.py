```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function with known good inputs and known bad inputs
values_good = [5, 3, 'three', (])
values_bad = [1, 'abc', (()), [1, 2, 3])

assert filter_integers(values_good) == [5, 3, 'three']
assert filter_integers(values_bad) == []
```  This Python code defines a function called filter_integers that takes a list of values as input and returns a new list containing only the integers from the input list. The function uses the language feature in Python, called typing, to check the types of each element in the input list. The test part of the function is then tested with two different lists of values to make sure that it works correctly and returns the correct output for all inputs.