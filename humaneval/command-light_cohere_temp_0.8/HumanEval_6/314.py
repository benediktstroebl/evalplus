```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with nested parentheses.
    Returns a strategic order of the list of deepest nesting level.
    Input: s - A string with multiple groups of parentheses separated by spaces.
    """
    Expected following format: {(())}, (...)

    Example:
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack: List[int] = []
    in_curly: int = 0
    for char in s:
        if char == '(':
            stack.append(in_cury)
            in_curly += 1
        elif char == ')':
            if len(stack) == 0:
                raise ValueError("Unexpected ')' without parentheses")
            out_level = stack.pop()
            if in_curly > out_level:
                stack.append(out_level)
                in_curly -= 1
    return stack
```