```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes in a string of multiple groups of parentheses separated by spaces.
    It returns a list of deepest level of nesting.
    """

    Input: A string of groups of parentheses separated by spaces.
    Output: A list of deepest level of nesting, where each element is a unique parent

    """
    stack = []
    for i, char in enumerate(parent_string, 1):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                    raise ValueError("Group without closing parenthesis")
            if len(stack) == 0:
                return []
    return stack
```