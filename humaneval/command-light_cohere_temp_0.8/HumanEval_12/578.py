```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string.
    >>> longest(['a', 'b', 'c']) 
    'a'
    >>> longest(['a', 'bb', 'ccc']) 
    'ccc'
    >>> longest([]) 
    None
    >>> longest(['a', 'aa', 'aaa']) 
    'aaa'
    """

    # Use built-in str.join() to convert all list of strings to a single string
    longest_str = ''.join()

    # Loop through list of strings and append each string to the growing result
    for string in strings:
        longest_str += string

    # Use str.isupper() to convert all string to uppercase (required by longest built-in function)
    longest_str = ''.upper(longest_str)

    return longest_str
```