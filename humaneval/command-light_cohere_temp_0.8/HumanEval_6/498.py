```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string of nested parentheses.
    Returns a level-of nesting of parentheses in a string.
    Args:
        string s: the string to parse for nested parentheses
    Returns:
    List[int], list of levels of nesting of parentheses in the string
    """
    stack: List[int] = []
    in_parenthesis: bool = False
    for char in s:
        if char == "(":
            if in_parenthesis:
                stack.append(1)
                in_parenthesis = True
            else:
                stack.append(0)
        elif char == ")":
                if not in_parenthesis:
                    stack.append(1)
                in_parenthesis = True
        else:
            if in_parenthesis:
                in_parenthesis = False
            else:
                stack.append(0)
    stack.append(1)
    return stack
```