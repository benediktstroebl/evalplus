```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of parentheses into individual strings.
    Args:
        s (str): input string containing parentheses.
    Returns: a list of strings without any nesting or extra spaces.
    """
Returns: A list of strings, each consisting of a balanced set of parentheses.
    """
    balanced set of parentheses means that each opening brace has an associated closing brace and no pair is nested within another.
    """
    balanced_string = []
    for i in range(0, len(s) - 1):
        if s[i] == '(' and s[i + 1] == ')':
            balanced_string.append(s[i])
            s[i], s[i + 1] = ''  # Remove pair from input
        else:
            balanced_string.append(s[i])
    balanced_string = ''.join(balanced_string)
    return balanced_string
```