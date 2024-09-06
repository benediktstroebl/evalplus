```python
# Importing the required module
from typing import List

# The function to be defined
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result

# Unit tests
def test_concatenate():
    """
    Test if the function 'concatenate' behaves as expected.
    """
    # Empty list should result in empty string
    assert concatenate([]) == ''

    # Single element in list should result in the element itself.
    assert concatenate(['a']) == 'a'

    # Multiple elements in list should be concatenated
    assert concatenate(['a', 'b', 'c']) == 'abc'

    # Result should handle unicode characters
    assert concatenate([u'α', u'β', u'π']) == u'αβπ'

# Calling the tests
test_concatenate()
```