```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(sorted(set(string), key=len, reverse=True))

# Test suite
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'bc', 'cd']
    assert all_prefixes('ab') == ['ab']
    assert all_prefixes('') == []
    assert all_prefixes('x') == []
test()
```
This code defines a function that calculates and returns a list of all prefixes from the shortest to the longest characters in the input string. It provides a testing to ensure the correctness of the function.