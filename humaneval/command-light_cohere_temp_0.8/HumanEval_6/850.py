```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                result.append(stack.pop()
            # now the unique, highest-level parentheses in stack)
            stack.pop()
       have empty stack, do not append a new item.
# Test Case
# Example test cases
def test_parse_nested_parens():
    test_cases = [
        "(()()) ((())) () ((()))()",
        "((())()())",
        "()()((()))",
        "((),())",
        "()()()(()",
        "(((),)))"
    ]
    for test_case in test_cases:
        parsed = parse_nested_parens(test_case)
        assert parsed == [2, 3, 1, 3]  # This should be the correct answer
test_parse_nested_parens()
```
This code defines a function `parse_nested_parens` that parses and depth-levels of nested parentheses in a given string `s`. The function uses a stack to keep track of the nesting level and pushes the current opening parent to the stack and appends the corresponding closing parent when encountered.

The function then returns a list of the deepest level of nesting of parentheses found in the string. This is to be the expected output based on the test cases provided in the `test_parse_nested_parens` function.