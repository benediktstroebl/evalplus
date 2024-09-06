```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates groups of parentheses into individual strings.

    Parameters:
    string s: Input string containing multiple groups of parentheses.
    Returns: list of strings: List of separated groups of parentheses
    """
    stack = []
    for char in s:
        if char == ' ':
            if not stack:
                stack.append('')
            else:
                stack.append('')
       
            else:
                stack.append(char)
   
    output = ''.join(stack)
    return output
```