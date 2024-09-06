```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
values_test1 = [1, 2, 3, 'abc', {}, [5], [()]]
result_test1 = filter_integers(values_test1)
assert result_test1 == [1, 2, 3]

# Test case 2: Filter integers from a tuple
values_test2 = ([1, 2, 3, 'abc'], [5])
result_test2 = filter_integers(values_test2)
assert result_test2 == ([1, 2, 3])

# Test case 3: Filter integers from a set
values_test3 = {1, 2, 3, 'abc'}
result_test3 = filter_integers(values_test3)
assert result_test3 == [1, 2, 3]

# Test case 4: Filter integers from an empty list
values_test4 = []
result_test4 = filter_integers(values_test4)
assert result_test4 == []

# This script defines a function **filter_integers** that takes a list of values as input and returns a new list containing only the integers from the input. The function is then type tested to ensure it is correct.
```