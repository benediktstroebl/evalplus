```python
from typing import List

def filter_integers(values:
    """
    filtered_integers = [x for x in values if isinstance(x, int)]
    return filtered_integers

# Test case 1: Basic filtering
test_case_basic = [1, 2, 3, 'abc', float('inf'), [{}]]
assert filter_integers(test_case_basic) == [1, 2, 3]

# Test case 2: Empty list
test_case_empty = []
assert filter_integers(test_case_empty) == []

# Test case 3: Filtering float values
test_case_float = [1, 2, 3. However, int() would return True for all values in this list
test_case_float_error = [3.14, 5]
with pytest. assert_raises(TypeError, filter_integers, test_case_float_error):

# Test case 4: Filtering empty dict
test_case_empty_dict = {}
assert filter_integers(test_case_empty_dict) == []
```
This script defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. It uses list comprehension to filter out non-integer values and then returns the filtered list. The test cases cover basic filtering, an empty list, filtering of float values, and an empty dict, with the expected results and error handling as mentioned.