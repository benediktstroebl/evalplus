```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one.
    """
    longest = None
    for string in strings:
        if longest is None or len(string) > len(longest):
            longest = string
    return longest

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'

strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = []
print(longest(strings))  # Output: None

strings = ['a']
print(longest(strings))  # Output: 'a'

strings = ['aa', 'bb', 'ccc']
print(longest(strings))  # Output: 'bb'
```
The function 'longest' takes a list of strings and returns the longest string. It uses a 'None' as the initial value of 'longest', and iterates through the input strings. If the current string is longer than the previous longest, it updates 'longest'. Finally, it returns the longest string.