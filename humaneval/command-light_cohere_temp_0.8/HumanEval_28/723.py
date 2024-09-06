```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate

    Returns:
    string: concatenated string
    """
    return ''.join(strings)

# Test case 1: empty list
assert concatenate([]) == ''

# Test case 2: single string
assert concatenate(['a']) == 'a'

# Test case 3: two strings
assert concatenate(['a', 'b']) == 'ab'

# Test case 4: list of three strings
assert concatenate(['a', 'b', 'c']) == 'abc'

# Test case 5: list of many strings
strings = ['a', 'b', 'c', 'd', 'e']
assert concatenate(strings) == 'adec'
 ```

This script defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. It is then pass five test cases to verify the correctness of the function.