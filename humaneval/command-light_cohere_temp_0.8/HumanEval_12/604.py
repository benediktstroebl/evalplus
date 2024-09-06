```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list.
    Parameters: strs is a list of strings.
    Returns the longest string in the list, or None if empty.
    """
    str match len(max(strings, key=len))

# Test cases
strings = ['a', 'bb', 'ccc']
print("Longest:", longest(strings))  # Output: "ccc"

strings = []
strings. strings strings.value_too = 'hello world'
print("Longest:", longest(strings))  # Output: None
```
The code defines a function `longest` that takes a list of strings as an argument and returns the longest string in the list. The `longest` function uses the `max` function to find the maximum length of the strings and uses the `key` argument of the `max` function to get the actual string value. The test cases demonstrate the value of the `longest` function.