```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings. Return list of empty if string is empty.
    """
    string s = input()
    if not s: return []
    opening_braces = '({[(){}[]}'
    closing_braces = ')'

    output = []
    for i, char in enumerate(s):
        if char == opening_braces[i % len(opening_braces)]:
            output.append(char)
        while (i+1 < len(s) and s[i+1] == closing_braces[0])
        if char == ' ':
            pass
        else:
            output.append(char)
    return output
```

This script defines a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate strings with properly separated parentheses. The function uses a opening and closing parentheses to create a mapping of when to add an open parenthesis or when to add a closing parenthesis.  The empty string input returns an empty list.