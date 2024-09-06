```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with multiple groups of nested parentheses separated by spaces.
    Returns a expected list of the deepest level of nesting.
    """

    test suite:
    Test cases with a variety of inputs.
    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    >>> parse_nested_parens('()  ((()))')
    []
    >>> parse_nested_parens('() () ((())))'))
    [1]
    >>> parse_nested_parens('(()()())()())()()()')
    [4, 4, 4, 4]
    """
    stack = []
    opening_paren = True
    for c in s:
        if c == '(' and opening_paren:
            stack.append(1)
            opening_paren = False
        elif c == ')' and not opening_paren:
            stack.pop()
        if len(stack) == 0:
            return [len(stack) - 1]
        elif c == ')' and opening_paren:
            stack.append(len(stack[-1])
            opening_paren = False
        elif c == '(':
            opening_paren = True
        else:
            raise ValueError("Unhandled character in parentheses: {}".format(c))
    return stack
```