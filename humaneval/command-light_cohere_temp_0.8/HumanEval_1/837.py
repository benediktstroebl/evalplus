```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return a list of separate parenthesis groups.
    """ Separate groups into balanced (each open brace is properly closed), and not nested within each other.
    """
    balanced = True
    for i, char in s:
        if char == '(' and balanced == True:
            balanced = False
        elif char == ')':
            if balanced == True:
                balanced = False
            else:
                break
        elif char == ' ' or char == '\n':
            pass
        else:
            balanced = False
    return ['(' + c + ')') for c in s if c == '(' and balanced]
```