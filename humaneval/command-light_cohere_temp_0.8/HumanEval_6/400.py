```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Input is a string of nested parentheses separated by spaces.
    This function will return the first level of nesting.
    """
    using list comprehension to iterate through the string
    """
    stack = []
    for c in s:
        if c == "(": stack.append(1)
        else: stack.append(0)
    while stack[-1] == 0)
    return stack[::-1]
```