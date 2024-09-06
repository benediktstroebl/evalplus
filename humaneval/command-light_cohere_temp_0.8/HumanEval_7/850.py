The provided Python code defines a function called **filter_by_substring** that filters a list of strings based on whether the substring is present within them.

This function takes a list of strings (**`strings`**) and a substring (**`substring`**) as input and returns a new list containing only the strings from the input list that contain the specified substring. 

The code is well-structured and follows good practices for designing Python functions. 

Here's the example of how you can use this function:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]
```