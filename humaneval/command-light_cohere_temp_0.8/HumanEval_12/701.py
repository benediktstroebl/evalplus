```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, returns the longest string.

    # empty list test
   
    if not strings:
        return None

    # find the length of the longest string
    max_length = 0
    longest_str = ""

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string

    return longest_str

# test cases
# list with one string
test_one = longest(['a'])
assert test_one == 'a'

# list with multiple strings of the same length
test_multi = longest(['aa', 'aa', 'aa'])
assert test_multi == 'aa'

# list with multiple strings of different lengths
test_diff = longest(['a', 'bb', 'ccc'])
assert test_diff == 'cc'

# empty list
test_empty = longest([])
assert test_empty is None
```