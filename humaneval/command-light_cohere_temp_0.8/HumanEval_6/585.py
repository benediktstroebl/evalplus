```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    for c in s:
        if c == '(': stack.push(0)
        elif c == ')': stack.pop()
        o:
            if stack: stack.pop()
            else: return []
    return stack

def test_parse_nested_parens():
    test_str = """(()())((()))()((())()())""
    result = parse_nested_parens(test_str)
    assert len(result) == [2, 3, 1, 3]
```

The code defines a `parse_nested_parens` function that parses a string of nested parentheses. The function uses a stack to keep track of open parentheses. It starts with the `push(0)` to start parsing and continues to pop the open parenthesis when it encounters a close parenthesis. The output is the deepest level of nesting of parentheses found in the string.

The `test_parse_nested_parens` function then creates a test string and passes it to the `parse_nested_parens` function. The function then returns the expected output and asserts that the output is correct using the assert statement.