```python
from typing import List
def longest(strings: List[str]): 
    """ Return the longest string in a list, or None if empty""" 
    if not strings: return None
    return max(strings, key=len)  # return the string with longest length as it is equal to len()

# Test cases
test_cases = [ ['a', 'b', 'c'], ['a', 'bb', 'ccc'], ['abc', 'abc'] ]

for text in test_cases: 
    result = longest(text)
    assert result == 'ccc' if text != [''] else None

print("All tests passed!")
```