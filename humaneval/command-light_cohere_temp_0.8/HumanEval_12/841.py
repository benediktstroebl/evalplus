```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.
    """
    takes a list of strings and returns the length of the longest string, or None if the list is empty.
    """
    list must contain at least string
    """

    # Tests
    strings = ['a', 'bb', 'ccc']
    assert longest(strings) == 3
    strings = []
    assert longest(strings) is None
    strings = ['aa']
    assert longest(strings) == 1
    strings = ['a', 'bc', '1111']
    assert longest(strings) == 3
    ```
The function `longest` takes a list of strings as input and returns the length of the longest string. It also has tests that the list is not empty and contains at least one string.