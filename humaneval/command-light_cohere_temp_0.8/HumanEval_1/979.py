```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates a string of parenthesis groups into individual strings.
    - Returns balanced and single open parenthesis to its corresponding closed parenthesis
    - Leaves no extra space between groups.
    """
    expects the first-level groups to be balanced and properly parenthes
    """
    stack = []
    result = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack or stack[-1] != char:
                result.append(char)
                stack.append(char)
            return result
    return result
```