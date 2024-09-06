```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all parenthesis groups, returns a list of individual elements.
    >>> separate_paren_groups(') ) (( )) (( )( ))'
    ['(', ')', '()()', '()']
    """
    return [part.split('()') for part in s.split(' '')]
```  This function splits the input string `s` into list `l` of substrings. It uses the string.run-time to split `s` using `()` and the backticks `()` to correctly split the parenthesis groups and return the list.