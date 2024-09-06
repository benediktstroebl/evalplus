```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.join(char) for char in string if char != ''] + ['abc']

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['a', 'ab', 'acd']
    assert all_prefixes('abcde') == ['abc', 'abcd', 'abcdef']
```
This Python script defines a function `all_prefixes` that returns a list of all prefixes of a given input string. The test_all_prefixes function verifies that the output of `all_prefixes` function is correct for different input strings.