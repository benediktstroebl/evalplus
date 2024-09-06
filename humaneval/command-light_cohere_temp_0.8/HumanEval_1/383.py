```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """ Function to separate and rearrange parentheses into separate strings.
    - Returns a balanced (each open brace is properly closed) and not nested within each other
    - Ignore any spaces in the input string.
    >>> ['()', '((()))', '(()())'] = separate_paren_groups('( ) (( )) (( )( ))')')
    """
    list = []
    stack = []
    current = ""
    for char in parentheses:
        if char == " ":
            stack.append(current)
            current = ""
        elif char == ")":
            if current:
                list.append(current)
                current = stack.pop()
                stack.append(current)
            current = ""
        else:
            current += char
    return list
```