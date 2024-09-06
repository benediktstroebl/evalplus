Here is a Python script that contains a self-contained function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [i for i in string if i != '' and i not in all_prefixes(string[1:])]

def all_prefixes_test() -> None:
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('') == []
    assert all_prefixes('xx') == ['x']
    assert all_prefixes('  ') == ['  ')
    assert all_prefixes('    x   ') == ['x', '    x   ']
```
The `all_prefixes` function computes the prefixes of the input string by iterating through each character and checking if the character is not empty and not in the list of prefixes from its substring. The `all_prefixes_test` function tests the `all_prefixes` function with various input strings and asserts the expected outputs.