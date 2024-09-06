```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list of values
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert [x for x in result_test1 if x == 5] == [5]

# Test case 2: Filter integers from a list of mixed data types
values_test2 = [1, 2, 3, 'abc', {}, []]
result_test2 = filter_integers(values_test2)
assert result_test2 == [1, 2, 3]

# Test case 3: Filter integers from an empty list
values_test3 = []
result_test3 = filter_integers(values_test3)
assert result_test3 == []
```
This script defines a function `filter_integers` that filters a list of values to include only the integers. The test cases demonstrate the other types of data, such as lists, strings, and empty lists, and the expected output.