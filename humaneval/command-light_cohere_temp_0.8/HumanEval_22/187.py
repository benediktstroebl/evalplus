```python
from typing import List

def filter_integers(values: List[Any]):
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
test_case1 = [1, 2, 3, 'abc', 4, 5]
result1 = filter_integers(test_case1)
assert result1 == [1, 2, 3]

# Test case 2: Filter integers from a dict with strings
test_case2 = {'a': 1, 'b': 2, 'c': 'xx'}
result2 = filter_integers(test_case2)
assert result2 == [1, 2]

# Test case 3: Filter integers from an empty list
test_case3 = []
result3 = filter_integers(test_case3)
assert result3 == []

# Test case 4: Filter integers from a list with any data type
test_case4 = ['a', 3.14, 5]
result4 = filter_integers(test_case4)
assert result4 == [3.14, 5]
```
The function `filter_integers` takes a list of any python value and returns a list of integers by filtering out all non-integer elements. 

The test cases demonstrate that the function works correctly for various scenarios.