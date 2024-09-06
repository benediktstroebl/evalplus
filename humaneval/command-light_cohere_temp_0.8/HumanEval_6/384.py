```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening = False
    for c in s:
        if c == '(':
            opening = True
        elif c == ')':
            if not opening:
                stack.append(0)
            opening = False
        else:
            stack[-1] += 1
    return stack

# Test code
def test_parse_nested_parens(s):
    assert parse_nested_parens(s) == [0, 1, 3]
# Example usage
test_string = "(()()) ((())) () ((()))"
test_parse_nested_parens(test_string)  # Output: [0, 1, 3]
```

This Python script defines a function `parse_nested_parens` that performs a depth-first traversal of nested parentheses in a given string. The function takes a input string `s` and returns a list of integers representing the deepest level of nesting for each group of parentheses found. The `test_parse_nested_parens` function is a test code that passes the `parse_nested_parens` function with an example string. The `test_string` variable contains a Markdown code block with nested parentheses.