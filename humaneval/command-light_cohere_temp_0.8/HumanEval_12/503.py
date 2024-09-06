Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    strings = [a'bb'ccc'
    """
    if not strings:
        return None
    
    max_length = max([len(string) for string in strings])
    longest_string = strings[0]
    for string in strings:
        if len(string) == max_length:
            longest_string = string
    return longest_string
```
This function takes a list of strings as input and returns the longest string found in the list. It also includes type hints, such as `strings = [a'bb'ccc']` to show the structure of the input list.