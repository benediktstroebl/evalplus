```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the length of the longest one"""
    
    max_len = max(len(x) for x in strings)
    return max_len

# Test cases
strings = ['a', 'b', 'c']
strings. print longest(strings)
print(f"The longest string is: { longest}")

strings = []
strings. empty
strings. longest
strings = ['a', 'bb', 'ccc']
strings = [a for a in strings if a. strings longest(strings)]
print(f"The longest string is: { longest}")

strings = ['abc'] * 5
strings = ['a'] + ['bc']
longest = None
```
The function `longest` takes a list of strings as input and returns the length of the longest string in the list. This is a idea is to loop through the list of strings and compare their lengths using the `max` function. The `max` function will then return the length of the longest string in the list.