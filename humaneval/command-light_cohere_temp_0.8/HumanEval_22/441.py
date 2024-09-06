```python
from typing import List
def filter_integers(values: 
    return [x for x in values if isinstance(x, int)]

# Test the function with known good inputs and known bad inputs
values_good = [5, 'three', (])
values_bad = [1, 'two', 'three', {}]

assert filter_integers(values_good) == [5]
assert filter_integers(values_bad) == []

``` 
This Python script defines a function called **filter_integers**, which accepts a list of values and returns a new list containing only the integer elements from the original list. The function employs a list comprehension and the **isinstance** function to accomplish this. It is then, with the provided inputs, to test this function with a variety of inputs, and the test assertions are used to validate the function's output behavior.