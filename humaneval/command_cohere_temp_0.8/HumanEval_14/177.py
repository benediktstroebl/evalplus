```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda s: s != '', string))));
```
The function utilizes the `dropwhile` function from the `itertools` module to eliminate elements from the beginning of the string iteratively until an empty string is encountered. The list of dropped prefixes is then reversed to ensure they are arranged in ascending order. This generates a list of prefixes from shortest to longest.

Here's a test to verify the correctness of the implementation:
```python
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('aaa') == ['', 'a', 'aa', 'aaa']
    assert all_prefixes('ab') == ['a', 'ab']
    assert all_prefixes('') == ['']
    assert all_prefixes('abcd') == ['a', 'ab', 'abc', 'abcd']
```