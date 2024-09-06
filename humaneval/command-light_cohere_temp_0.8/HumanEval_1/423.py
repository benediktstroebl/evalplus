```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of parentheses.
    Returns: list of separate strings after separating groups of parentheses.
    """
    balanced (each open brace is properly closed)
    """
    list_result = []
    current_group = []
    
    for char in s:
        if char == ')':  # Track open paren
            if current_group:  # Add current as part of new group
                list_result.append(''.join(current_group)
                current_group = []
            else:
                current_group.append(char)
        else:  # Add space character
                current_group.append(' ')
    
    if current_group:
        list_result.append(''.join(current_group)
    
    return list_result
```