```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: list of strings to concatenate
    :return: concatenated string
    """
    return ''.join(strings)

# Test case 1: empty list
assert concatenate([]) == ''

# Test case 2: single string
assert concatenate(['a']) == 'a'

# Test case 3: two strings
assert concatenate(['a', 'b']) == 'ab'

# Test case 4: list of strings
assert concatenate(['a', 'b', 'c']) == 'abc'
```
This script defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. It then passes four test cases to ensure the function is working correctly, which should pass.

Note that you can use this function in your markdown code block to solve the problem and get the result.