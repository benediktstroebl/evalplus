```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] != 1:
                raise ValueError("Unexpected closing parenthesis")
            result.append(stack.pop())
        stack.
        elif c == '(':
            stack.append(0)
        else:
            stack[-1] += 1
    return result

# Unit tests
def test_parse_nested_parens():
    test_cases = [
        "(()()) ((())) () ((())())",
        "()()()()()()()()()()()()()()() ()",
        "((()))",
        "()()())",
        "(())",
    ]
    for case in test_cases:
        parenthesis_list = parse_nested_parens(case)
        print(parenthesis_list)
```
This script defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. The function uses a stack to keep track of the opening and closing parentheses, and it iterates through the string, adding and removing parentheses as needed. The test_parse_nested_parens function contains a series of test cases that cover various scenarios.