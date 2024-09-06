```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values_test_case1 = ['a', 3.14, 5]
assert filter_integers(values_test_case1) == [5]

values_test_case2 = [1, 2, 3, 'abc', {}, []]
assert filter_integers(values_test_case2) == [1, 2, 3]

``` 
This script defines a function `filter_integers` that filters a list of values and returns only the integers from that list. It utilizes Python's type hints to provide information about the expected type of the input argument `values` and the return value.