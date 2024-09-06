```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, `strings`, as input and returns the longest string in the list. If the input list is empty, the function returns `None`. If there's only one string in the list, the function returns the only string (it doesn't matter what the string is). If there are multiple strings in the list, the function returns the longest one using the `max` function and a custom key function that determines the maximum string length.

Here's an example of how you might use this function:
```python
result = longest(['apple', 'banana', 'cherry', 'date'])
print(result)  # expected output: 'cherry'
```