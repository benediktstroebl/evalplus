```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string in the list.
    Return the string, or None if the list is empty.
    """
    return max(strings, key=len) if strings else None

# Test case 1
test_longest = ['a', 'bb', 'ccc']
result = longest(test_longest)
assert result == 'ccc'

# Test case 2
empty_list = []
result = longest(empty_list)
assert result is None

# Test case 3
same_strings = ['a', 'bb', 'ccc']
result = longest(same_strings)
assert result == 'a'
```
The above function takes a list of strings as an argument and returns the longest string in the list. It returns `None` if the list is empty. The function uses the maximum function with the `key` argument set to the `len` function to sort the strings in the list by length.