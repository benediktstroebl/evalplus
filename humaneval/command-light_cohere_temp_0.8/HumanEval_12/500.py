```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string in the list"""
    if not strings:
        return None
    max_len = max(len(str) for str in strings)
    return str(max_len)

# Unit tests for the longest function
strings = ['a', 'b', 'c']
longest_result = longest(strings)
assert longest_result == 'c'

strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
assert longest_result == 'ccc'
```
This code defines a function called `longest` that takes a list of strings as an argument and returns the length of the longest string in the list. The code then provides a unit tests to ensure the correctness of the `longest` function. 

Note:  This is a very simple and basic version of the longest function, and you can extend and improve it further based on your requirements and needs.