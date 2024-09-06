```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(itertools.chain_from_prefixes(string))

def itertools_chain_from_prefixes(string):
    """Chain all prefixes together."""
    return iter((''.join() for _ in range(len(string), 1, -1)))

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

def test_itertools_chain_from_prefixes():
    assert list(itertools_chain_from_prefixes('abc')) == ['a', 'ab', 'abc']

if __name__ == "__main__":
    test_all_prefixes()
    test_itertools_chain_from_prefixes()
```
This script provides a self-contained function and tests to solve the problem. It defines the function `all_prefixes` which returns a list of all prefixes in the input string from shortest to longest. The `itertools_chain_from_prefixes` function creates an iterator for concatenating prefixes of the input string in reverse order.