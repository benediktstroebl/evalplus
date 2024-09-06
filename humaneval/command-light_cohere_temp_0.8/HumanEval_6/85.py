```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for char in s:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                stack.pop()  #:
                    stack.append(0)
        else:
            return []
    return stack


# Unit tests
def test_parse_nested_parens():
    test_cases = [
        "(()()) ((())) () ((())()())",
        "((()))",
        "()((())())"
    ]

    for case in test_cases:
        actual = parse_nested_parens(case)
        expected = [2, 3, 1, 3]  # Values corresponding to the deepest level of nesting
        assert actual == expected


# Example usage
test_parse_nested_parens()
```

This script provides a function `parse_nested_parens` that accepts a string containing multiple groups of parentheses, separated by spaces. The function utilizes a stack to keep track of open parentheses and their corresponding levels. It then returns thears expected results corresponding to the deepest level of nesting in the input string.

The function is also accompanied by a set of unit tests using the `test_parse_nested_parens` function, which verifies that the `parse_nested_parens` function behaves correctly for various inputs.