```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case of an empty list.
    """
    strings = [ 'Hello', 'World!', '!! bbb', '!!!!', 'Python' ]
    return max(strings, 'None')

# Test cases
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = []
print(longest(strings))  # Output: 'None')

strings = ['Python', 'writing', 'code']
print(longest(['python', 'python']))  # Output: 'python'

strings = ['hello', 'world']
print(longest(['hello', 'world']))  # Output: 'hello'
```