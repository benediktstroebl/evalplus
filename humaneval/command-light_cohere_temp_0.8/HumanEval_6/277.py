```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with nested parentheses.
    Returns a process the levels of nesting, starting from the top-level deepest parentheses.
    """
    expected format: different groups of parentheses separated by spaces.
    For example: ((()()) ((())) )()
    """
    stack: List[int] = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
                if len(stack) == 0:
                    return []
                pop_level = stack.pop()
                if pop_level >= 2:
                    return []
                stack.append(pop_level)
    return stack
```