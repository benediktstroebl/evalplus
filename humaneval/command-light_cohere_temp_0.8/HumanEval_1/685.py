```python
from typing import List
def separate_paren_groups(parenthesis: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Return a balanced groups of parentheses separated by spaces as separate strings.
    """

    list of strings that are the separated parenthesis
    """
    stack = []
    out = []
    in_string = True
    for char in parenthesis:
        if char == ')':
            if not:
                stack.append(')')
                in_string = False
        elif in_string:
            out.append(char)
            in_string = False
        else:
            stack.append(char)

    return out
```