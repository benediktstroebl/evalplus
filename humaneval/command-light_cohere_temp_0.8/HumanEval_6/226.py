```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':  # match opening parenthesis
            stack.append(1)
        else:  # match closing parenthesis
            if len(stack) == 0:  # match closing parenthesis without nested
                output.append(0)
            else:  # match closing parenthesis with nested
                output.append(stack.pop())
            stack.pop()
        stack
        match closing parenthesis with nested group
    return output
def test_parse_nested_parens(s: str) -> None:
    assert parse_nested_parens(s) == [1, 3, 2, 3], "This is a test."
```

This script defines a function **parse_nested_parens** that parses a string of nested parentheses. It also provides a test function **test_parse_nested_parens** that asserts the correct parsing behavior of the parse_nested_parens function with an example string.