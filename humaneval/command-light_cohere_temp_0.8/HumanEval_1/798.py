```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates and returns a list of parenthesis groups in a string.
    >>> s = '()( )(( ))(( )( ))'
    >>> separate_paren_groups(s)
    ['()', '(())', '(()())']
    """
    return [p.replace(1, 0, 1) for p in s.split('() + '()')
```  The function takes a string s as input and returns a list of parenthesis groups. The algorithm works by splitting the input string into a list of characters, then searching for the sequence of '()' characters, and constructing a tuple with the start index, the end index, and the group itself.