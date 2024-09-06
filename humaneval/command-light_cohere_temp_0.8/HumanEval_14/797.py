```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ['a', 'ab', string[0]] + all_prefixes(string[1:])

def all_prefixes_test(string: str) -> None:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'cd', 'abcd']
    assert all_prefixes('xzyxws') == ['x', 'xy', 'xz', 'xws']
    assert len(all_prefixes('')) == 0
```
This script defines a function called `all_prefixes` that takes a string `string` as input and returns a list of all prefixes from shortest to longest. The function uses the example code to test the `all_prefixes` function.