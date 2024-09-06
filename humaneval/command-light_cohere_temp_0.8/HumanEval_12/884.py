```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of empty list or single string. """

   
    with_statement(is_positive_list(strings)):
        return max(strings, key=len)

# Test cases
with_statement(is_positive_list(['a', 'bb', 'ccc'])):
    assert longest(['a', 'bb', 'ccc']) == 'ccc'

with_statement(is_positive_list('abc')):
    assert longest(['abc']) == 'abc'

with_statement(is_positive_list([])):
    assert longest([]) is None

with_statement(is_positive_list('abcd')):
    assert longest('abcd') == 'abcd'

# Error cases
with_statement(is_positive_list(['ab'])):
    assert longest(['ab']) == 'ab'

with_statement(is_positive_list([1, 2, 3])):
    assert longest([1, 2, 3]) == 1
```
This Python script defines a function `longest` that takes a list of strings and returns the longest string from the list. It also includes various test cases to check the function's behavior for different scenarios, such as empty lists, single strings, and lists of strings. Additionally, error cases are added to demonstrate the function's behavior when the input is not valid.