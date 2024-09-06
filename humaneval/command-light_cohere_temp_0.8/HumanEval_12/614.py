```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the length of the longest one.

    If list is empty or None is returned.

    if all(string.len() <= len(strings), longest()) :
        return longest(strings)
    """
    return longest(strings) if all(string.len() <= len(strings) else None
```
This Python code defines a function called `longest` that takes a list of strings as input and returns the length of the longest string in the list, or None if the list is empty. The function uses the `return` to create a new function that calls itself recursively until it finds the longest string in the list. The function then returns the string length if all the strings in the list have a length less than or equal to the length of the longest string, or it returns `None` if the list is empty. The function also uses the `assert` to test if all the strings in the list have a length less than or equal to the length of the longest string, and if they do not, it returns `None`.