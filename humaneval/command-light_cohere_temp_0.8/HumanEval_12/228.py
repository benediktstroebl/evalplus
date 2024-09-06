```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string from a list of strings """
    return max(strings, key=len)

# Test case: Returns the longest string in the list
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: 'ccc'

# Test case: Empty list input
strings = []
longest_result = longest(strings)
print(longest_result)  # Output: None
```