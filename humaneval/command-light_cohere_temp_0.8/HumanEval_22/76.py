```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [element for element in values if isinstance(element, int)]

# Test case 1: Basic function usage
values1 = [1, 2, 3, 'abc', }
result1 = filter_integers(values1)
assert result1 == [1, 2, 3]

# Test case 2: Empty list
values2 = []
result2 = filter_integers(values2)
assert result2 == []

# Test case 3: List with non-integer elements
values3 = [1, 2, 3, 'four', 5]
result3 = filter_integers(values3)
assert result3 == [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integer elements from the original list. The test cases demonstrate the
1. A basic usage, where the function is applied to a list of numbers, and the expected result is the list of integers.

2. An empty list is This dry run.
3. A list with non-integer elements, which should be filtered and remain the empty list.