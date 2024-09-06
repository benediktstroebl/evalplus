```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    Function to parse a string of nested parentheses.
    Returns a list of the deepest levels of nesting.
    """

    given the string contains multiple groups of parentheses separated by spaces.
    Each group is opened by a left parenthesis, has a maximum of 3 items,
    and is closed by a right parenthesis or a space.
    """ Example string is ['()', '() ()', '()'])
    """
    stack: List[int] = []
    for char in parent_string:
        if char == '(':
            stack.append(1)
        else:
            if stack:
                opened, stack. Pop the top element from
                returned = stack.pop()
                if not opened:
                return []
        stack.append(char)
    if char == ')':
            if stack:
                # If not empty stack, this is the closing of a parenthesis group.
                opened, stack.
                stack.pop()
                the means in opened.
            return stack

    # Test suite
    test_strings = [
        '(()()) ((())) () ((())()())',
        '(())',
        '() ()',
        '(, )',
        '()()',
        '((()))'
    ]
    parsed = [parse_nested_parens(s) for s in test_strings]
    return parsed
```