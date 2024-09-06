Here's the Python script that includes the function with tests:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of an empty list. """

    test:
    assert longest(['a', 'b', 'c']) == 'a',
    assert longest(['a', 'bb', 'ccc']) == 'ccc',
    assert not longest([])
    assert longest(['aa', 'aa']) == 'aa'

    """ Return the longest string in the list """
    return max(strings, key=len)
```