```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in the list """
    if not strings:
        return None

    # Sort strings alphabetically
    strings.sort()
    string = ''.join(sorted(strings, key=str.len))

    if len(string) == 1:
        return string

    # No strings in the list
    return None

# Unit tests
def test_longest():
    return [ longest('abc') == 'abc',
                longest('aa') == 'aa',
                longest('') is None,
                longest(['a', 'bb', 'ccc']) == 'ccc' ]

test_longest()
 ```