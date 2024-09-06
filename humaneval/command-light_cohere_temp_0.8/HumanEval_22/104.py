```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values_test_case1 = ['a', 3.14, 5]
assert filter_integers(values_test_case1) == [5]

values_test_case2 = [1, 2, 3, 'abc', {}, []]
assert filter_integers(values_test_case2) == [1, 2, 3]

error_Case = [1, 2, 'aa', 3.14]
with pytest. assert.equal(filter_integers(error_Case)) as assertFalse:
    pass()
```
The function `filter_integers` takes a list of values as input and returns a new list that contains only the integers from the input list. 

It uses a list comprehension to filter out non-integer elements from the input list.