```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values1 = [1, 2, 3, 'abc', {}, [1, 2, 3, 'four'])
assert filter_integers(test_values1) == [1, 2, 3]

# Test case 2
test_values2 = [1, 2, 3, 'five', [1, 2, 3])
assert filter_integers(test_values2) == [1, 2, 3]

# Test case 3
test_values3 = [1, 2, 3, 4, 5, 6]
assert filter_integers(test_values3) == [1, 2, 3]
``` 
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It utilizes the filter to check if each element is an integer and then returns it in the new list.