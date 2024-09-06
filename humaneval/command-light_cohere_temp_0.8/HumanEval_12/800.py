```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from the list of strings.
    Parameters:
    strings (List[str]): List of strings
    Returns:
    List of strings, where each string is the longest one in the list
    """
    longest = str.maketransverse(strings)
    return longest

# test case 1
test_strings = ['a', 'b', 'c']
result = longest(test_strings)
assert result == 'c'

# test case 2
test_strings = ['a', 'bb', 'ccc']
result = longest(test_strings)
assert result == 'ccc'

# test case 3
test_strings = []
result = longest(test_strings)
assert result is None
```