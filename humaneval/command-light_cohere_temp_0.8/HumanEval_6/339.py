Here is a self-contained Python script that solves the problem you have provided:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with multiple groups of nested parentheses separated by spaces.
    Returns a nested list of the deepest level of nesting.
    >>> s = '(()()) ((())) () ((()))()'
    >>> parse_nested_parens(s)
    [2, 3, 1, 3]
    """
    stack: List[int] = []
    open_p: List[int] = []
    close_p: List[int] = []

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
            open_p.append(i)
        if char == ')':
                stack.pop()
                if stack:
                    if len(stack) == 0:
                        # All open parentheses are closed, reparse stack to get the final result.
                        for j in range(open_p):
                            if j != len(stack):
                                stack.append(open_p.pop() +
                        stack.pop()
                                open_p.pop()
                        if char == '('
                close_p.append(i)
            else:
                    open_p.append(i)
    if char == ')' and len(stack) == 0:
                    # All open parentheses are closed, return stack as result
                    return stack
    return stack
```