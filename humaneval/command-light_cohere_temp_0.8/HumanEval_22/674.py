```python
from typing import List

def filter_integers(values:
    """
    filtered_ints = []
    for value in values:
        if isinstance(value, int):
            filtered_ints.append(value)
    return filtered_ints

# Unit tests
test_filter_integers = [1, 2, 3, 'abc', [1.0, 2., 'abc', 5, {}]
result = filter_integers(test_filter_integers)
assert result == [1, 2, 3]
test_empty = []
result2 = filter_integers(test_empty)
assert result2 == []
test_single = [5]
result3 = filter_integers(test_single)
assert result3 == [5]
```
The function **`filter_integers`** accepts a list of values as input and returns a filtered list of integers. It then uses a filtering approach to do this, checking if each value is an integer and adding it to a new list. 

The unit tests at the end validate the function's behavior for different scenarios, such as empty lists, single values, and lists containing various data types.