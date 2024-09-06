```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    in_stack: bool = False
    for c in s:
        if c == '(' and not in_stack:
            in_stack = True
        elif c == ')':
            if in_stack:
                stack.append(level)
                in_stack = False
    return stack
def test_parse_nested_parens(s: str) -> None:
    for case in [
        "((())(()())())",
        "(()()())((()))",
        "((()()()))((()))",
        "(()()()())()",
        "()()()()()",
        "()()((())()())",
        "(()()((()))())",
        "((())((()))()())",
        "((()()()()((()))))",
        "((()))()()()()",
        "()((())()()()())",
        "((()())()())()()",
        "(()()()())()()",
        "()()()()()()",
        # invalid cases
    ]:
        parsed = parse_nested_parens(case)
        if parsed != [1, 3, 2]:
            raise AssertionError("Case %s should have nesting level [1,3,2], got %s" % (case, parsed))
```
The code defines a function `parse_nested_parens` that parses and returns the deepest level of nesting for a given string of parentheses.

The function uses a stack data structure to keep track of the nesting level and iterates through each character in the string.

The function tests the `parse_nested_parens` with a number of test cases, including valid and invalid cases. The tests ensure that function correctly parses the input and raises an AssertionError if the returned list does not match the expected nesting level.