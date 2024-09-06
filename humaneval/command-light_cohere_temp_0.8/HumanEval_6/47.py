```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of nested parentheses separated by spaces as input and returns the deepest level of nesting of parentheses.
    >>> example input: ('(()()) ((())) () ((()))()')
    >>> [2, 3, 1, 3]
    """
    stack: List[int] = []
    opening: List[str] = []
    closing: List[str] = []

    for char in paren_string:
        if char == ')':
            if stack:
                stack.append(stack.pop()
                done by opening for stack, closing)
                stack = []
                opening.append(char)
                closing.append(char)
            else:
                closing.append(char)
        elif char == '(':
            stack.append(1)
            opening.append(char)
            else:
                stack.append(int(stack))
                closing.append(char)

    return closing  # return final closing brackets
    ```