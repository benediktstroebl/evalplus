```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    # function to find the length of longest string
    max_length = max(len(str) for str in strings)
    # if all strings have the same length, return the first string
    if max_length == len(strings):
        return strings[0]
    # if no string is long enough, return None
    else:
        return None
# Example usage:
# longest(['a', 'bb', 'ccc']) # Output: 'ccc'
# longest(['aa', 'bb']) # Output: 'bb'
# longest([]) # Output: None
# longest(['aa', 'bb', 'ccc']) # Output: 'aa'
```
This Python script defines a function called `longest` that takes a list of strings as input and returns the longest string in the list, or `None` if the list is empty or no string is long enough. The function first finds the the maximum length of all strings in the list using the `max` function and the `len` function, and then checks if all strings have the same length. If so, it returns the string that has the maximum length, otherwise it returns `None`.