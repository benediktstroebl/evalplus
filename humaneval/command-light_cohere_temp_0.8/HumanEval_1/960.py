```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Separate balanced parentheses into a string and return the list of groups.
    >>> ')( )((()))' == '()'
    >>> ')) ))' (( )()' == '()('
    >>> '((()))()()' == '()('
    >>> '(((((()))))))' == '(())'
    >>> '(((((()))))()())())' == '()()()()'
    >>> '(((((()))))())()())( )' == '(()()()())'
    >>> '(((((((()))))))))' == '()(()())'
    >>> '(((((()))))()(), )())' == ['()', '(()())']
    """
    stack: List[str] = []
    new_str: str = ''
    for char in s:
        if char == ')':
            stack.append(new_str)
        new_str += char
        elif char == '(':
            new_str += char
        else:
            stack.push(new_str)
            new_str = ''
    return stack
```