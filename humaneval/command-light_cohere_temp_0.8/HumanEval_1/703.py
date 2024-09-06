```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string of parentheses as input and returns a list of separate and balanced parentheses
    As a static type, the input must be a string, and the output has no static type, as it's just a list of strings.
    """
    lists, but the input string into a list of opening parentheses, then iterates through the list of closing parentheses. Then, it uses the strings to check if it's a closing parent and if so, it appends it to the list.
    """
    list_ = []
    for c in s:
        if c == ')':
            list.append(c)
            if c == '(':
                continue
    return list
```