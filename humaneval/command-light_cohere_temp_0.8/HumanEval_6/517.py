```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input and returns a list of the deepest nesting levels.
    It will match the old-school:
    a) (())
    b) (()) (())
    c) (()) 

    It uses a stack data structure to keep track of nesting levels and the current opening parentheses.

    : Return a stack as a list of integers representing the deepest nesting levels.

    Input:
    s = '(()()) ((())) () ((())()())'
    :return: [3, 2, 1, 3]
    """

    stack: List[int] = []
    opening_parens = '(()()) ((())()())'

    for c in s:
        if c == opening_parens:
            stack.append(len)
        else:
            if stack and stack[-1] == '()':
                stack.pop()
           
                if c == ')' and len(stack) == 0:
                    stack.append(0)
            else:
                stack.append(int(c) if c.isalpha() else c))

    return stack