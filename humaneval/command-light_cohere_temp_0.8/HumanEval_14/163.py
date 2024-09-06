```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(sorted(set(string), key=len))

# Tests
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
This code provides a function all_prefixes that returns a list of all prefixes of a given string, sorted from shortest to longest. The test_all_prefixes function verifies that the function works correctly by comparing the output of the function with the correct result. 
This function is self-contained and does not rely on any external functions or modules, which means it can be easily imported and used in other scripts.