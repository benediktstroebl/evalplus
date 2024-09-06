```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all spaces and separate each balanced parentheses group into separate strings.

    : Input to this function is a string containing multiple groups of nested parentheses.

    Output: List of strings, where each string represents a balanced parentheses group.
    """
    balanced (each open brace is properly closed) and not nested within each other.
    """

    return [["()", "(())", "(()())"]
    """
    return [s[i:i+2] for i in range(0, len(s), 2)]
```