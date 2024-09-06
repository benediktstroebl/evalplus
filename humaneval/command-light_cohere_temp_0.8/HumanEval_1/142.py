```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of balanced parentheses from the input string.
    Args:
        s (str): string containing one or more groups of parentheses
    Returns:
    List of separated strings.
    """
    def get_groups(s: str) -> List[str]:
        groups = []
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    groups.append(''.append(char)
                    stack.clear()
       
            elif char == ' ':
                stack.append(char)
        else:
                stack.append(char)
        return groups
    return []
    return get_groups(s)
```