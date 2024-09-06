```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
values_list = [3.14, 5, 1, 2, 'abc']
result_list = filter_integers(values_list)
assert len(result_list) == 4, "Filtering integers from non-integer values failed."

# Test case 2: Filter integers from a tuple
values_tuple = (1, 2, 3, 'abc')
result_tuple = filter_integers(values_tuple)
assert len(result_tuple) == 3, "Filtering integers from non-integer values failed."

# Test case 3: Filter integers from a list of dictionaries
values_dict = {1: 2, 3, 'abc', []}
result_dict = filter_integers(values_dict)
assert len(result_dict) == 3, "Filtering integers from non-integer values failed."

# Test case 4: Filter integers from a list of empty list
values_empty_list = []
result_empty_list = filter_integers(values_empty_list)
assert len(result_empty_list) == 0, "Filtering integers from empty list failed."
```