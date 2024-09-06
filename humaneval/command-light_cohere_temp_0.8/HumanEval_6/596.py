```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string containing multiple groups of nested parentheses separated by spaces and returns the deepest level of nesting.
    """
    string should be in the format: (())(...) or ((()()))(...)
    Example: ([2, 3, 1, 3])
    """
    result = []
    stack = []
    for match in s:
        if match == '(':
            stack.append(match)
        else:
            if stack:
                stack.pop()
                result.append(stack[-1:])
            stack = []
    return result
```