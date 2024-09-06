```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)

# Test case: empty list
test_case1:
    assert concatenate([]) == ''

# Test case: single string
test_case2:
    assert concatenate(['a']) == 'a'

# Test case: list of strings
test_case3:
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Test case: list of non-string elements
test_case4:
    assert concatenate([1, 2, 3]) == '123'
```
This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It provides several test cases to test the correctness of the function, which passes all the tests.