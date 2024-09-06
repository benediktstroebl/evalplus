```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :type strings: List[str]
    :rtype: str
    """
    return ''.join(strings)

# Test cases
strings = ['a', 'b', 'c']
test_concat = concatenate(strings)
assert test_concat == 'abc', "Test failed: " + test_concat +""

strings = []
test_concat = concatenate(strings)
assert test_concat == '', "Test failed: " + test_concat +""

strings = ['a']
test_concat = concatenate(strings)
assert test_concat == 'a', "Test failed: " + test_concat +""

strings = ['a', '!']
test_concat = concatenate(strings)
assert test_concat == 'a.!', "Test failed: " + test_concat +""

print("All tests passed!")
```