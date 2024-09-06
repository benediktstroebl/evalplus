```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string of nested parentheses.
    Returns a structure of nested parentheses
    """
    stack = []
    open_parens = ['(',')', '[]', '{}']
    for char in s:
        if char in open_parens:
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:  # unmatched closing parent
                raise ValueError("Unmatched closing parent")
        elif char in ['+', '-', '.', '/']:
            stack.append(char)
        else:
            raise ValueError("Unexpected character in parentheses")
    return stack

def test_parse_nested_parens():
    # Sample input for testing
    s = "(()()) ((())) () ((())()())"
    expected = [2, 3, 1, 3]
    got = parse_nested_parens(s)
    assert expected == got
```