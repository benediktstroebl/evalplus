```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function takes in a string of parenthesis groups and returns the deepest level of nesting of the parentheses.
    Parameters:
    parenthesis_string (str): The string of parenthesis groups to parse

    Returns:
    List[int]: A list of the deepest level of nesting of parentheses in each group.
    """
    List[int): A list of the deepest level of nesting of parentheses in each group
    """
    stack = []
    in_group = False
    parentheses_levels = []

    for char in parentheses_string:
        if char == '(':
            if not in_group:
                stack.append(1)
            in_group = True
        else:
            stack.append(0)
            in_group = False

        if char == ')':
            if len(stack) == 0 or stack[-1] == 0:
                raise ValueError("Unexpected closing parenthesis without a preceding opening parenthesis.")
            else:
                stack.pop()
                stack.
            parentheses_levels.append(stack[-1])

    return parentheses_levels
```