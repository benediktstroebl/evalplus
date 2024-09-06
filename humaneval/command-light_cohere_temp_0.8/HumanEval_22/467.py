```python
from typing import List
def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [i for i in values if isinstance(i, int)]

# Test the function
values_test = [1, 2, 3, 'abc', {}, []]
result_test = filter_integers(values_test)
assert result_test == [1, 2, 3]

# Another test with other data types
values_other = ['a', 3.14, 5]
result_other = filter_integers(values_other)
assert isinstance(result_other, list), "filter_integers returned non-list"
``` 
This script defines a function **filter_integers** that accepts a list of values and returns a new list containing only the integers from the input. The test cases demonstrate how the the function works by iterating through the input list and selecting only the integers.