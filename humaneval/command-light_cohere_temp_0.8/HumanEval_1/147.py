```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.
    Returns a time list of the strings.
    """
    open and close parentheses without any spaces.
    """
The function uses list comprehension and str.join to convert each parenthesis group into a string.
    """
    example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [str.join(x("(" + p + ")" for p in s.group[1:]) for group in zip(s.group(1::),]
    ]
```