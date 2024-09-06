```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string.
    >>> returns 'ccc'
    """

    if not strings:
        return None

    # sort the strings
    strings.sort()
    strings.filter(str.isalpha() == strings[max())

    # take the first one
    return strings[0]

# test cases
test_longest = []
test_longest.append(['a', 'b', 'c'])
test_longest.append(['aa', 'bb', 'ccc'])
test_longest.append([None])
test_longest.append(['ab'])
test_longest.append(['abc'])
test_longest.append(['aa', 'ccc'])

# validate the function
assert longest(test_longest) == 'ccc'
```