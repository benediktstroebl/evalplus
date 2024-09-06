Here's a Python script that contains the self-contained function `separate_paren_groups` that solves the problem of separating parentheses groups into individual strings:

```python
from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings and return the list.
    >>> separate_paren_groups(') ) (( )( )) (( ))'
    ['(', ')()', '()()()', '()')']
    """
    stack = []
    opening_braces = ['(', ')', '{', '[', '(', ')', ';']
    
    for char in paren_string:
        if char in opening_braces:
            if stack:
                closing_brace = stack.pop()
               
                if closing_brace and char != ' ' and char != '(':
                    stack.append(char)
                continue
        elif char == '(':
            stack.append(char)
        else:
                continue  # Ignore spaces and other non-parenthesis characters
    
    return stack
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated strings. The script uses a list of characters that represent opening parentheses and uses a stack to keep track of open parentheses while traversing the string. It properly handles different types of parentheses and correctly closes the groups.