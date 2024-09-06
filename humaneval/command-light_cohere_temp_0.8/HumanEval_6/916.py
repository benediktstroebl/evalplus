```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function is designed to parse a string of nested parentheses.
    Each group of parentheses are separated by a space, and the function returns a list of the deepest level of nesting for each group.

    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    """
    result = []
    stack = []
    in_open = False
    for c in s:
        if c == '(' and not in_open:
            stack.append(1)
            in_open = True
        elif c == ')':
            if len(stack) == 0:
                in_open = False
            else:
                stack.pop()
                result.append(stack[-1])
        stack.append(1)
    return result
```
The parse_nested_parens function is designed to parse a string of nested parentheses and return a list of the deepest level of nesting for each group. The function works by maintaining a stack of open parentheses and a boolean flag to indicate whether we are inside a group.

The function iterates over each character in the input string. It checks for the open parentheses and, if not, adds the current character to the stack. Then, it checks for closed parentheses and, if the stack is empty, it sets the flag to indicate that we are no longer inside a group. If the current character is a close parentheses, it pops the last element from the stack, appends the open parent to the stack, and appends the closed parent to the stack.

Finally, the function returns the result, which is a list of the deepest level of nesting for each group of parentheses.