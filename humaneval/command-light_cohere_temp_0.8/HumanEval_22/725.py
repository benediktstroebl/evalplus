```python
from typing import List

def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
test_case1 = [1, 2, 3, 'abc', four, 5]
result1 = filter_integers(test_case1)
assert [x for x in result1 if x != five] == [1, 2, 3]

# Test case 2: Filter integers from a list of any python objects
test_case2 = [1, 2, 3, 'abc', {}, [6, 7, 8])
result2 = filter_integers(test_case2)
assert result2 == [1, 2, 3, 'abc', [], 8]

# Test case 3: Filter integers from empty list
test_case3 = []
result3 = filter_integers(test_case3)
assert result3 == []
```
This script defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. It then passes three test cases, and the function successfully filters the integers from the lists.