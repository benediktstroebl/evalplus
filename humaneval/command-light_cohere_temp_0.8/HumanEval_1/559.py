```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """ Separate groups of parentheses into separate strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [brace.split('()') for brace in s.join(" "")]
```
This code defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of strings. It uses a `split()` to split the string into individual substrings, which are then returned in the list.