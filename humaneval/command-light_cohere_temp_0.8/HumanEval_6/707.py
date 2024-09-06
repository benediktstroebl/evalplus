```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function parses a string with multiple groups of nested parentheses separated by spaces.
    It returns the strategy: start from the first pair and push the level of nesting until we reach a closing pair.
    For example: Input: (())()((()))).
    Output: [2, 3]

    """
    stack = []
    in_parentheses = False
    nesting_levels = 0
    for c in s:
        if c == '(':
            if not in parenthesis_stack:
                nesting_levels += 1
                stack.append(nesting_levels)
                in_parentheses = True
            else:
                stack.append(nesting_levels)
                in_parentheses = False
        elif c == ')':
            if in_parentheses:
                nesting_levels -= 1
                stack.pop()
                in_parentheses = False
            else:
                stack.append(nesting_levels)
                in_parentheses = True
    return stack
```