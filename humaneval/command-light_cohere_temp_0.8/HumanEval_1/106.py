```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate balanced parentheses from the string.
    Each group of parentheses should be separated as a separate string.
    Returns a balanced groups of parentheses as a list of strings.
    """
    open_pa, close_pa, *gp = []
    for i, char in enumerate(s):
        if char == '(' and s[i+1] == ')':
            open_pa.append(char)
            close_pa.append(s[i+1])
        elif char == ')':
            close_pa.append(char)
        else:
            gp.append(char)
    return gp
```