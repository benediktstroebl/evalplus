```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.
    strings = ['a', 'bb', 'a']
    print(longest(strings))  # Output should be 'a'
    strings = ['a', 'bb', 'ccc']
    print(longest(strings))  # Output should be 'ccc'
    strings = ['aa', 'bb', 'bc', 'acc', 'ab']
    print(longest(strings))  # Output should be 'acc'
    strings = []
    print(longest(strings))  # Output should be None
    ```