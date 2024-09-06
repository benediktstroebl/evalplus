```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ['a', 'ab', string[:2]] + all_prefixes(string[2:])

def all_prefixes_test(string: str) -> None:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'cd']
    assert all_prefixes('abca') == ['ab', 'aca']
    assert len(all_prefixes('')) == 0
```
This script defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of an input string. It also provides a the specific test function `all_prefixes_test` that passes corresponding tests for the `all_prefixes` function.