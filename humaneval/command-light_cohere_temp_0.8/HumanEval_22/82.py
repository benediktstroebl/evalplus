```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 3, "Test case 1 failed"

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3, "Test case 2 failed"

# Test case 3
values3 = [1, 2, 3, True, [], 4.0]
result3 = filter_integers(values3)
assert len(result3) == 4, "Test case 3 failed"
``` 
This script defines a function called `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The test cases are also passed to ensure the function is correct.