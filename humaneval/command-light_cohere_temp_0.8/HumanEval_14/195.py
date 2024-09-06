Here is a self-contained Python script that defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.joincenter(string) for i in range(1, len(string)+1)][::-1]

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
test_prefixes()
```