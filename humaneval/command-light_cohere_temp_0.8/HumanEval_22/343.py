```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
test_filter_integers = [
    [],  # [] -> [] of_integers
    ['a', 3, 'abc', 5],  # str, int, float -> []
    [1, 2, 3],        # [1, 2, 3] -> [1, 2, 3]
    [1, 2, 'abc'],    # [1, 2] -> [1, 2]
    [1, 2, 3, 4, 5],  # Multiple values -> [1, 2, 3, 4]
]

# Function Usage and Testing
assert filter_integers(test_filter_integers) == [1, 2, 3]
assert not filter_integers(test_filter_integers[1:]) == []
assert filter_integers([1, 2, 'abc']) == [1, 2]
assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4]
```
This script provides a function filter_integers that filters a list of any Python values (values), returning only the integers. The test cases cover a filtering empty lists, strings, floats, and specific values, with the expected results. The function is then tested using the provided test cases.