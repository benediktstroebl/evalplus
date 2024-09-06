```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string in the list
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=str.antic_length)

# For unit tests
test_longest = []
test_longest.push_strings('a'.join()
test_longest.push_strings('bb'.join()
test_longest.push_strings('ccc'.join())
test_longest.push_strings('1234567890')
test_longest.push_strings('abc')
test_longest.push_strings('z')
test_longest.push_strings('aa')
test_longest.push_strings('CCC')

def test():
    assert longest(test_longest) == 'ccc'

test()
```